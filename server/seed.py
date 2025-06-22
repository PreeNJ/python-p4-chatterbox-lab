#!/usr/bin/env python3

from random import randint, choice as rc
from faker import Faker
from app import app
from models import db, Message

fake = Faker()

with app.app_context():
    
    print("Starting seed...")
    
    # Delete existing messages
    Message.query.delete()
    
    print("Creating messages...")
    
    messages = []
    
    # Create some sample messages
    usernames = ["Liza", "Duane", "Alice", "Bob", "Charlie", "Diana"]
    
    sample_messages = [
        "Hello 👋",
        "Hi brother",
        "let's get this chat app working",
        "i've got this!",
        "You got this! 💪",
        "How's everyone doing today?",
        "Great to see everyone here!",
        "This chat app is looking good!",
        "Nice work on the frontend!",
        "Ready to build the backend?",
        "Flask is awesome for APIs",
        "Let's make this work together"
    ]
    
    for i in range(12):
        message = Message(
            body=sample_messages[i] if i < len(sample_messages) else fake.sentence(),
            username=rc(usernames),
        )
        messages.append(message)
    
    db.session.add_all(messages)
    db.session.commit()
    
    print("Seeding complete!")
    print(f"Created {len(messages)} messages")