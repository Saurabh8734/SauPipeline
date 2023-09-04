from setuptools import setup, find_packages



setup(name="census-income", 
      version = "0.0.1",
      author="Saurabh Wabale",
      author_email="saurabhwabale8734@gmail.com",
      packages= find_packages(),
      install_requires = ["pandas", "numpy", "flask"]


)