#getting base image
FROM ubuntu
FROM python

MAINTAINER oscar dolloway <oscar.dolloway@hotmail.co.uk>

RUN mkdir helloworld


#RUN apt-get update
#RUN apt-get install -y git
#RUN apt install python3-pip
RUN pip install scipy
RUN pip install numpy
RUN pip install matplotlib
RUN pip install BeautifulSoup4
RUN pip install requests
#RUN pip install opencv
RUN pip install opencv-python

RUN git clone https://github.com/OscarDolloway/Video-Capture-assignement.git helloworld
RUN cd helloworld
RUN ls

CMD python helloworld/ImgProcTech.py




