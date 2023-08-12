from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Clean folder program by Python',
      url='https://github.com/IamSerJanGO/home_work_GoIT/blob/main/sorted-script.py',
      author='Serhi Sierov',
      author_email='None',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['clean-folder=clean_folder.sorted_script:main']}
      )
