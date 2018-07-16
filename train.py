from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import config.cfg as cfg 
from solver.solver_cifar import Solver
from network.vgg import VggNet
from data.dataset import cifar_dataset

import argparse 
import tensorflow as tf 

parser = argparse.ArgumentParser()
parser.add_argument('--lr',type=float,default=0.01,help='cifar_10 learning_rate')
parser.add_argument('--batch_size',type=int,default=64,help='batch size')
parser.add_argument('--moment',type=float,default=0.9,help='sovler moment')
parser.add_argument('--display_step',type=int,default=10,help='show train display')
parser.add_argument('--num_epochs',type=int,default=200,help='train epochs')
parser.add_argument('--predict_step',type=int,default=500,help='predict step')
parser.add_argument('--net',type=str,default='Vgg',help='net style')


def main(_):
	common_params = cfg.merge_params(FLAGS)
	print(common_params)
	dataset = cifar_dataset(common_params,cfg.dataset_params)
	network = VggNet('VGG16')
	solver = Solver(network,dataset,cfg.common_params)
	solver.solve()

if __name__=='__main__':
	FLAGS,unknown = parser.parse_known_args()
	tf.logging.set_verbosity(tf.logging.INFO)
	tf.app.run(main)