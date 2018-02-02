# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:35:22 2018

@author: cc
"""

import argparse

"""
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo
"""
"""
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
        print "verbosity turned on"
#-v后的参数保存在args.verbosity中

"""

#不需要加参数
"""
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
        print "verbosity turned on"
"""

#x为待输入的参数，以整数表示
"""
parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help="the base")
args = parser.parse_args()
answer = args.x ** 2
print answer
"""
#限定取值范围
"""
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
#以choices作为备选项目
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
#可以设置默认值：default
#parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], default=1,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
"""
#关于help信息的定义
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()#group作为互斥
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print answer
elif args.verbose:
    print "{} to the power {} equals {}".format(args.x, args.y, answer)
else:
    print "{}^{} == {}".format(args.x, args.y, answer)

#处理多余字符串的方法
"""
import argparse 
parser = argparse.ArgumentParser() 
parser.add_argument( 
    '--flag_int', 
    type=float, 
    default=0.01, 
    help='flag_int.' 
) 
FLAGS, unparsed = parser.parse_known_args() 
print(FLAGS) 
print(unparsed)
"""






