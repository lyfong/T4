import click
from t4 import app,db
from t4.models import Messages

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    '''init all database.'''
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    click.echo('droped..')
    db.create_all()
    click.echo('created..')

    fake = Faker(locale='zh_CN')
    click.echo('Working...')

    ii=0

    for i in range(count):
        ii += 1
        t = Messages(
            id=ii,
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(t)

    db.session.commit()
    click.echo('Created %d fake messages.' % count)
