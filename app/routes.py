from flask import Flask, render_template, request, redirect, url_for
from app import app

import json
import sqlite3
import time

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Blog page
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Extracurriculars page
@app.route('/clubs')
def clubs():
    return render_template('clubs.html')

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Courses
@app.route('/aer')
def aer():
    return render_template('aer201.html')

@app.route('/civ')
def civ():
    return render_template('civ102.html')

@app.route('/praxis')
def praxis():
    return render_template('praxis.html')


# Projects
@app.route('/boxhead')
def game():
    return render_template('game.html')

@app.route('/parking')
def parking():
    return render_template('parking.html')

@app.route('/research')
def research():
    return render_template('research.html')


# Extracurriculars
@app.route('/deep')
def deep():
    return render_template('deep.html')

@app.route('/ewb')
def ewb():
    return render_template('ewb.html')

@app.route('/fes')
def fes():
    return render_template('fes.html')

@app.route('/ilead')
def ilead():
    return render_template('ilead.html')

@app.route('/solarcar')
def solarcar():
    return render_template('solarcar.html')

@app.route('/swim')
def swim():
    return render_template('swim.html')

@app.route('/toastmasters')
def toastmasters():
    return render_template('toastmasters.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')