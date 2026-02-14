from flask import Blueprint, render_template, request, redirect, url_for, flash
from epl import db
from epl.models import Player, Club

players_bp = Blueprint('players', __name__, url_prefix='/players')

@players_bp.route('')
def all_players():
  players = db.session.scalars(db.select(Player)).all()
  return render_template('players/index.html',
                         title='Players Page',
                         players=players)

@players_bp.route('/new', methods=['GET', 'POST'])
def new_player():
  clubs = db.session.scalars(db.select(Club)).all()
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    nationality = request.form['nationality']
    goal = int(request.form['goals'])
    squad_no = int(request.form['squad_no'])
    img = request.form['img']
    club_id = int(request.form['club_id'])
    # clean_sheets is optional (used for Goalkeepers). Accept empty input as None.
    cs_raw = request.form.get('clean_sheets', '')
    clean_sheets = int(cs_raw) if cs_raw and cs_raw.strip() != '' else None

    player = Player(name=name, position=position, nationality=nationality,
                    goal=goal, squad_no=squad_no, img=img, club_id=club_id,
                    clean_sheets=clean_sheets)
    db.session.add(player)
    db.session.commit()
    flash('add new player successfully', 'success')
    return redirect(url_for('players.all_players'))

  return render_template('players/new_player.html',
                         title='New Player Page',
                         clubs=clubs)

@players_bp.route('/search', methods=['GET', 'POST'])
def search_player():
  if request.method == 'POST':
    player_name = request.form.get('player_name', '')
    if player_name:
      players = db.session.scalars(db.select(Player).where(Player.name.like(f'%{player_name}%'))).all()
    else:
      players = []
    return render_template('players/search_player.html',
                           title='Search Player Page',
                           players=players)
  
  return render_template('players/search_player.html',
                        title='Search Player Page',
                        players=[])

@players_bp.route('/<int:id>/info')
def info_player(id):
  player = db.session.get(Player, id)
  return render_template('players/info_player.html',
                         title='Info Player Page',
                         player=player)

@players_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update_player(id):
  player = db.session.get(Player, id)
  clubs = db.session.scalars(db.select(Club)).all()
  if request.method == 'POST':
    name = request.form['name']
    position = request.form['position']
    nationality = request.form['nationality']
    goal = int(request.form['goals'])
    squad_no = int(request.form['squad_no'])
    img = request.form['img']
    club_id = int(request.form['club_id'])
    # clean_sheets handling
    cs_raw = request.form.get('clean_sheets', '')
    clean_sheets = int(cs_raw) if cs_raw and cs_raw.strip() != '' else None

    player.name = name
    player.position = position
    player.nationality = nationality
    player.goal = goal
    player.clean_sheets = clean_sheets
    player.squad_no = squad_no
    player.img = img
    player.club_id = club_id

    db.session.add(player)
    db.session.commit()

    flash('update player successfully', 'success')
    return redirect(url_for('players.all_players'))
  
  return render_template('players/update_player.html',
                         title='Update Player Page',
                         player=player,
                         clubs=clubs)


@players_bp.route('/<int:id>/delete', methods=['POST'])
def delete_player(id):
  player = db.session.get(Player, id)
  if not player:
    flash('Player not found', 'danger')
    return redirect(url_for('players.all_players'))

  db.session.delete(player)
  db.session.commit()
  flash('Player deleted successfully', 'success')
  return redirect(url_for('players.all_players'))
