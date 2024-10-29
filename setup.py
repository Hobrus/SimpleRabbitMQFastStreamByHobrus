from setuptools import setup, find_packages

setup(
    name='hobrus_rabbitmq',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'faststream[rabbit]'
    ],
    description='Простой пакет для работы с RabbitMQ с использованием FastStream',
    author='Suhobrus Boris',
    author_email='bhobrus@gmail.com',
    url='https://github.com/Hobrus/SimpleRabbitMQFastStreamByHobrus',
)