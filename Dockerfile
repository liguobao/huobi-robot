FROM python:3
RUN pip3 install pyyaml
RUN pip3 install flask
RUN pip3 install werobot
RUN pip3 install cryptography
RUN pip3 install redis
RUN pip3 install wxpy
RUN pip3 install requests
ADD . /app
WORKDIR /app
CMD [ "python3", "wechat_robot.py" ]
