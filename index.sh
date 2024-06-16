# Both these environment variables should be initialized before use
# You should also add
# 0 18 * * * PATH_TO_SCRIPT > /dev/null 2>&1
# to your crontab

source $INDEX_CONDA_ENVIRONMENT
python $INDEX_SCRIPT_PATH
conda deactivate
