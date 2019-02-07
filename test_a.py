from subprocess import check_call

check_call('python -m test_b', shell=True, env={'PYTHONPATH': 'foo'})
