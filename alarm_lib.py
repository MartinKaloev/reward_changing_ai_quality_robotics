#this is snipet explaining when you will get fail or not 
#insert this snipet to your path fiding algorithms after reshaping as external lib!





import numpy as np

#def value for a failing aka value causing failuar
def fail_alarm(ar_f,fail_v):
	a=np.array(ar_f)
	sum_a=np.sum(a)
	fail_value=fail_v*sum_a
	return fail_value

#def camparanse function showing that robot will cross forbiden areas if they offer shorted path
def comp(ar_f,fail_v,path_v):
	if fail_alarm(ar_f,fail_v) > path_v:
		return True
	else:
		return False

print(comp(ar_f,fail_v_path_v))
