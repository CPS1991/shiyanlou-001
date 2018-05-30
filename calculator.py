#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv # 用于写入csv文件

# 处理命令行参数类
class Args(object):
    def __init__(self):
        args_l = sys.argv[1:]

        index_c = args_l.index('-c')
        self.c = args_l[index_c + 1]
        index_d = args_l.index('-d')
        self.d = args_l[index_d + 1]
        index_o = args_l.index('-o')
        self.o = args_l[index_o +1]

args = Args()

#配置文件类
class Config:
    def __init__(self):
        self.config = self._read_config()

    # 配置文件读取内部函数
    def _read_config(self):
        config_d = {'s_total':0}
        with open(args.c) as file:
            for n_s in file.readlines():
                n_s_sp = n_s.split('=')
                num,sal = n_s_sp[0].strip,n_s_sp[1].strip()
                #print(num, sal)
                if num == 'JiShuL' or num == 'JiShuH':
                    config_d[num] = float(sal)
                else:
                    config_d['s_total'] += float(sal)
        return config_d

config = config().config

def calc_tax(sal):
    sal_i = int(sal)
    shebao = sal_i * config.get('s_total')
    #print(shebao)
    #print(config.get('JiShuL'))
    if sal_i < config.get('JiShuL'):
        shebao = config['JiShuL'] * config.get('s_total')
    if sal_i > config.get('JiShuH'):
        shebao = config['JiShuH'] * config.get('s_total')
    tax0 = sal_i - shebao - 3500
    if tax0 <0:
        tax =0
    elif tax0 <= 1500:
        tax = tax0 * 0.03 - 0
    elif tax0 <= 4500:
        tax = tax0 * 0.1 -105
    elif tax0 <= 9000:
        tax = tax0 * 0.2 -555
    elif tax0 <= 35000:
        tax = tax0 * 0.25 - 1005
    elif tax0 <= 55000:
        tax = tax0 * 0.3 -2755
    elif tax0 <= 80000:
        tax = tax0 * 0.35 - 5505
    else:
        tax = tax0 * 0.45 - 13505
    salary = sal_i - shebao - tax
    return [sal_i,format(shebao,'.2f'),format(tax,'.2f'),format(salary,'.2f')]

class Data:
    def __init__(self):
        with open(args.d) as file:
            data_l = list(csv.reader(file))
        self.value = data_l

data = Data().value
#print(data)

with open(args.o, 'w') as file:
    for i,s in data:
        baobiao = calc_tax(s)
        baobiao.insert(0,i)
        csv.writer(file).writerow(baobiao)



