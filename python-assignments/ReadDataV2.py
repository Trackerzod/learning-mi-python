"""Reads data... Duh..."""

import pandas as pd
import time

def read_data_file(filename, debug = False):
    t0 = time.process_time()
    f = open(filename, "r")

    for i in range(0, 32):
        line = f.readline()

    columnLine = f.readline().strip()
    t1 = time.process_time()
    f.close()

    # Strip unneeded columns
    columns = columnLine.split("\t")
    wantColumns = []

    for idx in range(len(columns)):
        if columns[idx].find("Comment_") == -1:
            wantColumns.append(idx)
    t2 = time.process_time()

    data = pd.read_csv(filename, delimiter="\t", na_values='-', skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,
    22,23,24,25,26,27,28,29,30,31,33], usecols=)
    t3 = time.process_time()

    if debug:
        print((
            f'File: {filename}\n'
            f'Shape: {data.shape} (Total: {data.shape[0] * data.shape[1]})\n'
            f'Timing information\n'
            f'  Reading header: {t1 - t0}s\n'
            f'  Column filtering: {t2 - t1}s\n'
            f'  Reading and parsing data: {t3 - t2}s\n'
            f'  Total: {t3 - t0}s\n'
        ))

    return data

def run_test(filename):
    data = read_data_file(filename, debug=True)

time.process_time()
