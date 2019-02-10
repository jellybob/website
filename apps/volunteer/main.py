# encoding=utf-8
from flask import redirect, url_for, render_template

from . import volunteer
from ..common import feature_flag, feature_enabled

@volunteer.route('/')
@feature_flag('VOLUNTEERS_SIGNUP')
def main():
    if feature_enabled("VOLUNTEERS_SCHEDULE"):
        return redirect(url_for('.schedule'))
    else:
        return redirect(url_for('.sign_up'))

@volunteer.route('/safeguarding')
@feature_flag('VOLUNTEERS_SIGNUP')
def safeguarding():
    return render_template('volunteer/safeguarding.html')

@volunteer.route('/info')
@feature_flag('VOLUNTEERS_SIGNUP')
def info():
    return render_template('volunteer/info.html')
