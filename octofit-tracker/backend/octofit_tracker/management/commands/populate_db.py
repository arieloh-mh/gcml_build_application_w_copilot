
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction
from pymongo import MongoClient

class Command(BaseCommand):
	help = 'Populate the octofit_db database with test data'

	def handle(self, *args, **options):
		# Eliminar completamente las colecciones para evitar conflictos de _id
		client = MongoClient('mongodb://localhost:27017/')
		db = client['octofit_db']
		for collection in ['activity', 'workout', 'leaderboard', 'user', 'team']:
			db.drop_collection(collection)

		with transaction.atomic():
			self.stdout.write(self.style.WARNING('Dropped old collections with pymongo.'))
			self.stdout.write(self.style.SUCCESS('Creating teams...'))
			marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
			dc = Team.objects.create(name='DC', description='DC superheroes')

			self.stdout.write(self.style.SUCCESS('Creating users...'))
			users = []
			users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel))
			users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel))
			users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc))
			users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc))

			self.stdout.write(self.style.SUCCESS('Creating activities...'))
			Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-20')
			Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-19')
			Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2026-02-18')
			Activity.objects.create(user=users[3], type='Yoga', duration=40, date='2026-02-17')

			self.stdout.write(self.style.SUCCESS('Creating workouts...'))
			w1 = Workout.objects.create(name='Full Body', description='Full body workout')
			w2 = Workout.objects.create(name='Cardio Blast', description='Intense cardio')
			w1.suggested_for.set([users[0], users[2]])
			w2.suggested_for.set([users[1], users[3]])

			self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
			Leaderboard.objects.create(team=marvel, points=150)
			Leaderboard.objects.create(team=dc, points=120)

			self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
