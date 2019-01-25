#coding:utf-8
import includes.mathexo as maths
import includes.lambdaFunc as lambdas
import includes.simpleFunc as funcs
import includes.execption_mod as excepts
import classes.template1 as env

env1=env.Environement("forest","A forest is plenty of yard and trees where live animals","Animal")

env1.desc()
print(env.Environement.world)
env.Environement.cworld("Mars")
print(env.Environement.world)
env.Environement.helloEnv()