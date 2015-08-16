from fabric.api import env, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts


@task
def check():
    env.platform_family = detect.detect()

    assert package.installed("td-agent")
    assert file.exists("/etc/td-agent/td-agent.conf")
    assert port.is_listening(8888)
    assert port.is_listening(24224)
    assert user.exists("td-agent")
    assert group.is_exists("td-agent")
    assert user.is_belonging_group("td-agent", "td-agent")
    assert process.is_up("ruby")
    assert service.is_enabled("td-agent")


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
