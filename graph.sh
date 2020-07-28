bonobo inspect --graph pipeline.py > pipeline.dot
dot -o etl.png -T png etl.dot