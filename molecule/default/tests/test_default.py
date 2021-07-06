import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_htpdate_service(host):
    htpdate = host.service("htpdate")
    assert htpdate.is_running
    assert htpdate.is_enabled


def test_htpdate_env_file(host):
    env_file = host.file("/etc/default/htpdate")
    assert env_file.exists
    assert oct(env_file.mode) == "0o644"
