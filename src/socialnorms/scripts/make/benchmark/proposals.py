"""Create candidate instances for the socialnorms benchmark.

This script takes in the socialnorms corpus and creates candidate
instances for the socialnorms benchmark of ranked action pairs. The
proposals then must be annotated using Mechanical Turk.
"""

import json
import logging
import os
import random

import click
import tqdm

from .... import settings, utils
from ....data.action import Action


logger = logging.getLogger(__name__)


# main function

@click.command()
@click.argument(
    'corpus_dir',
    type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.argument(
    'proposals_dir',
    type=click.Path(exists=False, file_okay=False, dir_okay=True))
@click.option(
    '--rounds', type=int, default=3,
    help='The number of rounds of random matchings to run. Each round'
         ' uses every action from the benchmark once. So, k rounds will'
         ' use an action at most k times. Defaults to 3.')
def proposals(
        corpus_dir: str,
        proposals_dir: str,
        rounds: int
) -> None:
    """Propose and write instances for the benchmark to PROPOSALS_DIR.

    Read in the socialnorms corpus from CORPUS_DIR and then for each
    split in the corpus, randomly pair actions together and write them
    to PROPOSALS_DIR in a format ready for being annotated on Mechanical
    Turk.
    """
    # Create the output directory
    os.makedirs(proposals_dir)

    # Iterate over each split of the corpus, creating the benchmark data
    # for each.
    for split in settings.SPLITS:
        logger.info(f'Reading the {split} split from the corpus.')

        ids_actions = []
        corpus_split_path = os.path.join(
            corpus_dir,
            settings.CORPUS_FILENAME_TEMPLATE.format(split=split['name']))
        with open(corpus_split_path, 'r') as corpus_split_file:
            for ln in tqdm.tqdm(corpus_split_file, **settings.TQDM_KWARGS):
                row = json.loads(ln)
                if row['action'] is not None:
                    action = Action(**row['action'])
                    if action.is_good:
                        ids_actions.append((row['id'], action))

        logger.info(f'Computing random matchings for {rounds} rounds.')

        instances = []
        for _ in range(rounds):
            random.shuffle(ids_actions)
            for i in range(0, len(ids_actions) - 1, 2):
                instances.append({
                    'id': utils.make_id(),
                    'actions': [
                        {
                            'id': id_,
                            'description': action.description
                        }
                        for id_, action in ids_actions[i:i+2]
                    ]
                })

        logger.info(f'Writing proposals to {proposals_dir}.')

        proposals_split_path = os.path.join(
            proposals_dir,
            settings.PROPOSALS_FILENAME_TEMPLATE.format(split=split['name']))
        with open(proposals_split_path, 'w') as proposals_split_file:
            for i in range(0, len(instances), settings.N_INSTANCES_PER_HIT):
                proposals_split_file.write(json.dumps({
                    'instances': instances[i:i+settings.N_INSTANCES_PER_HIT]
                }) + '\n')
