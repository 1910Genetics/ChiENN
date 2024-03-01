from setuptools import setup, find_packages

setup(
    name='chienn',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here.
        # They will be installed by pip when your project is installed.
        # 'requests',
        # 'numpy>=1.18.5',
        # etc.
    ],
    # Additional metadata about your package.
    description='Chiral GNN Model, Layer, and Featurizers for Molecular Property Prediction',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important for rendering the README in Markdown
    author='Piotr Gainski',
    author_email='piotr.gainski@doctoral.uj.edu.pl',
    # More information can be added here, such as 'url', 'license', etc.
)
