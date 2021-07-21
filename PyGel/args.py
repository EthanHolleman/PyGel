from argparse import ArgumentParser
import sys
from typing import Type

def parse_args():

    args = ArgumentParser('Simulate agarose gels')
    args.add_argument('dna', nargs='+', default=[], help='Path to genbank or fasta files of DNA sequences to run on gel.')
    args.add_argument('--gel-percent', default=0.07, help='Agarose concentration of gel.')
    args.add_argument('--lane-names', default=[], nargs='+', help='Lane names.')
    args.add_argument('--RE', default=[], nargs='+', action='append',
                      help='List of restriction endonucleases to cut sequences \
                      with. Defaults to no cutters. To set all sequences to be cut \
                      by the same enzymes pass --RE once with one list of cutters.\
                      To cut each lane with different enzymes pass --RE followed by \
                      the cutters to use multiple times.')

    cmd_args = args.parse_args()
    check_args(cmd_args)
    return cmd_args

def check_args(cmd_args):
    check_lane_names_length(cmd_args)
    check_cutters(cmd_args)


def check_lane_names_length(cmd_args):
    # lane names should have same length
    # as the number of sequences passed to dna arg
    if cmd_args.lane_names:
        if len(cmd_args.lane_names) != len(cmd_args.dna):
            raise TypeError('Must have same number of lane names as sequences!')


def check_cutters(cmd_args):
    if cmd_args.RE:
        if len(cmd_args.RE) > 1 and len(cmd_args.RE) != len(cmd_args.dna):
            raise TypeError('If specifying different cutters for each lane, \
                the number of specified lanes (number of times you pass --RE) \
                needs to equal the number of sequences. Control lanes \
                (undigested) can be specified by passing "CNTRL" instead of an \
                enzyme name')
    