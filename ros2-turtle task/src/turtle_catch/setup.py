from setuptools import find_packages, setup

package_name = 'turtle_catch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omarwaleed',
    maintainer_email='155390963+Omarsens@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [   'turtle_control = turtle_catch.turtle_control:main',
        'turtle_spawner = turtle_catch.turtle_spawner:main',
        'collision_detection = turtle_catch.collision_detection:main',
        ],
    },
)
