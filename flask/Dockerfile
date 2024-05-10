FROM python:3.13.0b1-alpine

# upgrade pip
RUN pip install --upgrade pip

# get curl and supervisor
RUN apk add supervisor curl

# permissions, logging, cron job, and nonroot user stuff
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log
WORKDIR /home/app
RUN echo "* * * * * /bin/sh /home/app/scripts/reload.sh" | crontab -u nonroot -
USER nonroot

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# poetry is fucking stupid
ENV PYTHON_KEYRING_BACKEN=Dkeyring.backends.null.Keyring
RUN mkdir -p /home/nonroot/.config/pypoetry/
RUN mv configs/auth.toml /home/nonroot/.config/pypoetry/auth.toml
RUN mv configs/supervisord.conf /home/app/

# python setup and installing deps
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt
RUN pip install /home/app/concrete_calculator
RUN cd /home/app/calculator_wrapper && poetry install && poetry update setuptools pip build && cd /home/app/
# poetry config certificates.fakepypi.cert /home/app/certs/publickey.crt
USER root
COPY configs/pip.conf /etc/pip.conf
RUN chown root:root /etc/pip.conf

CMD ["supervisord"]
