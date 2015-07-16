__author__ = 'Agostino Sturaro'

import os
import csv
import logging
import numpy as np
import shared_functions as sf

this_dir = os.path.normpath(os.path.dirname(__file__))
os.chdir(this_dir)
sf.setup_logging('logging_base_conf.json')
logger = logging.getLogger(__name__)

index_fpath = os.path.normpath('../Simulations/exp_1000n_many/tran_atk/1_cc/realistic/_index.tsv')
aggregate_fpath = os.path.normpath('../Simulations/exp_1000n_many/tran_atk/1_cc/realistic/_stats.tsv')

with open(index_fpath, 'r') as index_file, open(aggregate_fpath, 'wb') as aggregate_file:
    aggregate = csv.writer(aggregate_file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
    aggregate.writerow(['Instance_type', 'Indep_var_val', 'Dep_var_avg', 'Dep_var_std_dev'])

    index = csv.DictReader(index_file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
    for line in index:
        stats_fpath = line['Results_file']
        stats = np.genfromtxt(stats_fpath, delimiter='\t', skip_header=1, dtype=None)

        # access the first column according to the different structures numpy can output
        logger.debug('stats = {}'.format(stats))
        values = sf.get_unnamed_numpy_col(stats, 0)

        avg = np.average(values)
        std_dev = np.std(values)
        aggregate.writerow([line['Instance_type'], line['Indep_var_val'], avg, std_dev])
