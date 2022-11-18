from invoke import task

@task
def installPoetry(c):
    c.run("poetry install")

@task
def check(c):
    c.run("python3.8 -m compileall olivapp/")