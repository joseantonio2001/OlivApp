from invoke import task

@task
def installPoetry(c):
    c.run("poetry install")