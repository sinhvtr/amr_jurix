#!/bin/bash
#SBATCH -J g_2m -C K80 --partition=gpu --gres=gpu:1 --time=5-00:00:00 --output=train.out --error=train.err
#SBATCH --mem=80GB
#SBATCH -c 5

export PYTHONPATH=/home/sinhvtr/python/py27/bin/python

# python src_g2s/G2S_trainer.py --config_path config_max.json
# python src_g2s/G2S_trainer.py --config_path config/config_original_50ep.json
python src_g2s/G2S_trainer.py --config_path config/config_g2s_ldc_civil_gen1.json