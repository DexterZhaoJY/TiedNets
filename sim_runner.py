__author__ = 'Agostino Sturaro'

import os
import filecmp
import shared_functions as sf
import cascades_sim as cs

this_dir = os.path.dirname(__file__)
logging_conf_fpath = os.path.join(this_dir, 'logging_base_conf.json')

sim_conf_fpath = 'test_sets/ex_1_full/run_realistic.ini'
exp_log_fpath = 'test_sets/ex_1_full/exp_log_realistic.txt'

# when
sf.setup_logging(logging_conf_fpath)
cs.run(sim_conf_fpath)

# then
print filecmp.cmp('log.txt', exp_log_fpath, False)  # assuming UNIX EOLs are used