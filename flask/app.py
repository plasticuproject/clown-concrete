"""app.py"""

from typing import Any
from werkzeug.exceptions import NotFound, InternalServerError
from werkzeug.wrappers import Response
from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from flask import (Flask, request, render_template, send_from_directory, flash,
                   redirect, url_for)
from layout_utils import set_menu

# Stupid hack to stabilize challenge
calculator: Any
try:
    from calculator_wrapper import Calculator
    calculator = Calculator()
except ImportError:
    from backup_calculator_wrapper import Calculator as BackUpCalculator
    calculator = BackUpCalculator()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
csrf = SeaSurf(app)

SELF = "'self'"
csp = {
    'default-src': SELF,
    'img-src': [SELF, 'data:'],
    'script-src': [
        SELF,
        'cdn.jsdelivr.net',
    ],
    'style-src': [SELF, 'cdn.jsdelivr.net'],
}
Talisman(
    app,
    force_https=False,
    content_security_policy=csp,
    content_security_policy_nonce_in=['script-src', 'style-src'],
)


@app.errorhandler(404)
def not_found(error: NotFound) -> Response:
    """Redirect all 404 errors to index."""
    # pylint: disable=unused-argument
    return redirect(url_for('index'))


@app.errorhandler(500)
def internal_server_error(error: InternalServerError) -> Response:
    """Handle Internal Server Errors."""
    # pylint: disable=unused-argument
    return redirect(url_for('index'))


@app.route('/')
def index() -> str:
    """/"""
    m_c = set_menu('home')
    return render_template('home/index.html', mc=m_c, clown=True)


@app.route('/calculators/square_slab')
def square_slab() -> str:
    """/calculatores/square_slab"""
    return render_template('calculators/square_slab.html', mc={}, clown=False)


@app.route('/calculators/wall')
def wall() -> str:
    """/calculators/wall"""
    return render_template('calculators/wall.html', mc={}, clown=False)


@app.route('/calculators/footer')
def footer() -> str:
    """/calculators/footer"""
    return render_template('calculators/footer.html', mc={}, clown=False)


@app.route('/calculators/square_column')
def square_column() -> str:
    """/calculators/square_column"""
    return render_template('calculators/square_column.html',
                           mc={},
                           clown=False)


@app.route('/calculators/round_slab')
def round_slab() -> str:
    """/calculators/round_slab"""
    return render_template('calculators/round_slab.html', mc={}, clown=False)


@app.route('/calculators/round_column')
def round_column() -> str:
    """/calculators/round_column"""
    return render_template('calculators/round_column.html', mc={}, clown=False)


@app.route('/calculators/steps')
def steps() -> str:
    """/calculators/steps"""
    return render_template('calculators/steps.html', mc={}, clown=False)


@app.route('/calculators/curbs_and_gutters')
def curbs_and_gutters() -> str:
    """/calculators/curbs_and_gutters"""
    return render_template('calculators/curbs_and_gutters.html',
                           mc={},
                           clown=False)


@app.route('/about')
def about() -> str:
    """/about"""
    m_c = set_menu('about')
    return render_template('home/about.html', mc=m_c, clown=False)


@app.route('/about/concrete_calculator_source')
def c_c_source() -> Response:
    """/about/concrete_calculator_source"""
    return send_from_directory('sources/',
                               'concrete_calculator.zip',
                               as_attachment=True)


@app.route('/about/calculator_wrapper_source')
def c_w_source() -> Response:
    """/about/calculator_wrapper_source"""
    return send_from_directory('sources/',
                               'calculator_wrapper.zip',
                               as_attachment=True)


@app.route('/calculate/<structure>', methods=['GET', 'POST'])
def calculate(structure: str) -> Response:
    """/calculate/<structure>"""
    # pylint: disable=too-many-branches
    structures = ('square_slab', 'wall', 'footer', 'square_column',
                  'round_slab', 'round_column', 'steps', 'curbs_and_gutters')
    units_dict = {'ft': 'feet', 'yd': 'yards', 'm': 'meters'}
    flash_text_error = 'Please enter numerical measurments only.'

    if structure not in structures:
        return redirect(url_for('index'))

    if request.method == 'POST':
        try:
            units = request.form['units']
            for key in request.form:
                if key not in ('units', '_csrf_token'):
                    float(request.form[key])
            _ = units_dict[units]
        except (ValueError, KeyError):
            flash(flash_text_error)
            return redirect(url_for(structure))

        if structure == 'square_slab':
            value = calculator.square_slab(length=float(
                request.form['length']),
                                           width=float(request.form['width']),
                                           depth=float(request.form['depth']),
                                           units=units)

        elif structure == 'wall':
            value = calculator.wall(length=float(request.form['length']),
                                    thickness=float(request.form['thickness']),
                                    height=float(request.form['height']),
                                    units=units)

        elif structure == 'footer':
            value = calculator.footer(length=float(request.form['length']),
                                      width=float(request.form['width']),
                                      depth=float(request.form['depth']),
                                      units=units)

        elif structure == 'square_column':
            value = calculator.square_column(
                length=float(request.form['length']),
                width=float(request.form['width']),
                height=float(request.form['height']),
                units=units)

        elif structure == 'round_slab':
            value = calculator.round_slab(diameter=float(
                request.form['diameter']),
                                          depth=float(request.form['depth']),
                                          units=units)

        elif structure == 'round_column':
            value = calculator.round_column(diameter=float(
                request.form['diameter']),
                                            depth=float(request.form['depth']),
                                            units=units)

        elif structure == 'steps':
            value = calculator.steps(platform_depth=float(
                request.form['platform_depth']),
                                     run=float(request.form['run']),
                                     rise=float(request.form['rise']),
                                     width=float(request.form['width']),
                                     steps=int(request.form['steps']),
                                     units=units)

        elif structure == 'curbs_and_gutters':
            value = calculator.curbs_and_gutters(
                curb_depth=float(request.form['curb_depth']),
                curb_height=float(request.form['curb_height']),
                gutter_width=float(request.form['gutter_width']),
                flag_thickness=float(request.form['flag_thickness']),
                length=float(request.form['length']),
                units=units)

        flash(f'Requires {value} cubic {units_dict[units]} of concrete.')
    return redirect(url_for(structure))
