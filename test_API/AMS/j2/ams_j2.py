# -*- coding: utf-8 -*-
"""Base workchain"""
import os
from aiida import orm, load_profile
from aiida.engine import submit
from aiida_uppasd.workflows.magnon_spectra import UppASDMagnonSpectraRestartWorkflow

load_profile()
current_path = os.getcwd()

exchange_1 = '''1 2 -1 -1 -1 1.839624404 0.866
1 2 0 -1 -1 1.839624404 0.866
1 2 -1 0 -1 1.839624404 0.866
1 2 0 0 -1 1.839624404 0.866
1 2 -1 -1 0 1.839624404 0.866
1 2 0 -1 0 1.839624404 0.866
1 2 -1 0 0 1.839624404 0.866
1 2 0 0 0 1.839624404 0.866
1 1 0 0 -1 0.031818272 1.000
1 1 0 -1 0 0.035489955 1.000
1 1 -1 0 0 0.034829027 1.000
1 1 1 0 0 0.034829027 1.000
1 1 0 1 0 0.035489955 1.000
1 1 0 0 1 0.031818272 1.000
2 1 0 0 0 1.839624404 0.866
2 1 1 0 0 1.839624404 0.866
2 1 0 1 0 1.839624404 0.866
2 1 1 1 0 1.839624404 0.866
2 1 0 0 1 1.839624404 0.866
2 1 1 0 1 1.839624404 0.866
2 1 0 1 1 1.839624404 0.866
2 1 1 1 1 1.839624404 0.866
2 2 0 0 -1 0.059966387 1.000
2 2 0 -1 0 0.060562684 1.000
2 2 -1 0 0 0.061050289 1.000
2 2 1 0 0 0.061050289 1.000
2 2 0 1 0 0.060562684 1.000
2 2 0 0 1 0.059966387 1.000'''
exchange_2 = '''1 1 0 -1 -1 0.080402816 1.414
1 1 -1 0 -1 0.081281445 1.414
1 1 1 0 -1 0.081281445 1.414
1 1 0 1 -1 0.080402816 1.414
1 1 -1 -1 0 0.079846493 1.414
1 1 1 -1 0 0.079846493 1.414
1 1 -1 1 0 0.079846493 1.414
1 1 1 1 0 0.079846493 1.414
1 1 0 -1 1 0.080402816 1.414
1 1 -1 0 1 0.081281445 1.414
1 1 1 0 1 0.081281445 1.414
1 1 0 1 1 0.080402816 1.414
1 2 -1 -1 -2 0.110748457 1.658
1 2 0 -1 -2 0.110748457 1.658
1 2 -1 0 -2 0.110748457 1.658
1 2 0 0 -2 0.110748457 1.658
1 2 -1 -2 -1 0.110678298 1.658
1 2 0 -2 -1 0.110678298 1.658
1 2 -2 -1 -1 0.110736026 1.658
1 2 1 -1 -1 0.110736026 1.658
1 2 -2 0 -1 0.110736026 1.658
1 2 1 0 -1 0.110736026 1.658
1 2 -1 1 -1 0.110678298 1.658
1 2 0 1 -1 0.110678298 1.658
1 2 -1 -2 0 0.110678298 1.658
1 2 0 -2 0 0.110678298 1.658
1 2 -2 -1 0 0.110736026 1.658
1 2 1 -1 0 0.110736026 1.658
1 2 -2 0 0 0.110736026 1.658
1 2 1 0 0 0.110736026 1.658
1 2 -1 1 0 0.110678298 1.658
1 2 0 1 0 0.110678298 1.658
1 2 -1 -1 1 0.110748457 1.658
1 2 0 -1 1 0.110748457 1.658
1 2 -1 0 1 0.110748457 1.658
1 2 0 0 1 0.110748457 1.658
2 2 0 -1 -1 0.035945477 1.414
2 2 -1 0 -1 0.036069315 1.414
2 2 1 0 -1 0.036069315 1.414
2 2 0 1 -1 0.035945477 1.414
2 2 -1 -1 0 0.035730514 1.414
2 2 1 -1 0 0.035730514 1.414
2 2 -1 1 0 0.035730514 1.414
2 2 1 1 0 0.035730514 1.414
2 2 0 -1 1 0.035945477 1.414
2 2 -1 0 1 0.036069315 1.414
2 2 1 0 1 0.036069315 1.414
2 2 0 1 1 0.035945477 1.414
2 1 0 0 -1 0.110748457 1.658
2 1 1 0 -1 0.110748457 1.658
2 1 0 1 -1 0.110748457 1.658
2 1 1 1 -1 0.110748457 1.658
2 1 0 -1 0 0.110678298 1.658
2 1 1 -1 0 0.110678298 1.658
2 1 -1 0 0 0.110736026 1.658
2 1 2 0 0 0.110736026 1.658
2 1 -1 1 0 0.110736026 1.658
2 1 2 1 0 0.110736026 1.658
2 1 0 2 0 0.110678298 1.658
2 1 1 2 0 0.110678298 1.658
2 1 0 -1 1 0.110678298 1.658
2 1 1 -1 1 0.110678298 1.658
2 1 -1 0 1 0.110736026 1.658
2 1 2 0 1 0.110736026 1.658
2 1 -1 1 1 0.110736026 1.658
2 1 2 1 1 0.110736026 1.658
2 1 0 2 1 0.110678298 1.658
2 1 1 2 1 0.110678298 1.658
2 1 0 0 2 0.110748457 1.658
2 1 1 0 2 0.110748457 1.658
2 1 0 1 2 0.110748457 1.658
2 1 1 1 2 0.110748457 1.658'''
exchange_3 = '''1 1 -1 -1 -1 -0.226616190 1.732
1 1 1 -1 -1 -0.226616190 1.732
1 1 -1 1 -1 -0.226616190 1.732
1 1 1 1 -1 -0.226616190 1.732
1 1 -1 -1 1 -0.226616190 1.732
1 1 1 -1 1 -0.226616190 1.732
1 1 -1 1 1 -0.226616190 1.732
1 1 1 1 1 -0.226616190 1.732
1 2 -1 -2 -2 -0.005551829 2.179
1 2 0 -2 -2 -0.005551829 2.179
1 2 -2 -1 -2 -0.005455077 2.179
1 2 1 -1 -2 -0.005455077 2.179
1 2 -2 0 -2 -0.005455077 2.179
1 2 1 0 -2 -0.005455077 2.179
1 2 -1 1 -2 -0.005551829 2.179
1 2 0 1 -2 -0.005551829 2.179
1 2 -2 -2 -1 -0.005530290 2.179
1 2 1 -2 -1 -0.005530290 2.179
1 2 -2 1 -1 -0.005530290 2.179
1 2 1 1 -1 -0.005530290 2.179
1 2 -2 -2 0 -0.005530290 2.179
1 2 1 -2 0 -0.005530290 2.179
1 2 -2 1 0 -0.005530290 2.179
1 2 1 1 0 -0.005530290 2.179
1 2 -1 -2 1 -0.005551829 2.179
1 2 0 -2 1 -0.005551829 2.179
1 2 -2 -1 1 -0.005455077 2.179
1 2 1 -1 1 -0.005455077 2.179
1 2 -2 0 1 -0.005455077 2.179
1 2 1 0 1 -0.005455077 2.179
1 2 -1 1 1 -0.005551829 2.179
1 2 0 1 1 -0.005551829 2.179
2 1 0 -1 -1 -0.005551829 2.179
2 1 1 -1 -1 -0.005551829 2.179
2 1 -1 0 -1 -0.005455077 2.179
2 1 2 0 -1 -0.005455077 2.179
2 1 -1 1 -1 -0.005455077 2.179
2 1 2 1 -1 -0.005455077 2.179
2 1 0 2 -1 -0.005551829 2.179
2 1 1 2 -1 -0.005551829 2.179
2 1 -1 -1 0 -0.005530290 2.179
2 1 2 -1 0 -0.005530290 2.179
2 1 -1 2 0 -0.005530290 2.179
2 1 2 2 0 -0.005530290 2.179
2 1 -1 -1 1 -0.005530290 2.179
2 1 2 -1 1 -0.005530290 2.179
2 1 -1 2 1 -0.005530290 2.179
2 1 2 2 1 -0.005530290 2.179
2 1 0 -1 2 -0.005551829 2.179
2 1 1 -1 2 -0.005551829 2.179
2 1 -1 0 2 -0.005455077 2.179
2 1 2 0 2 -0.005455077 2.179
2 1 -1 1 2 -0.005455077 2.179
2 1 2 1 2 -0.005455077 2.179
2 1 0 2 2 -0.005551829 2.179
2 1 1 2 2 -0.005551829 2.179
2 2 -1 -1 -1 -0.045906218 1.732
2 2 1 -1 -1 -0.045906218 1.732
2 2 -1 1 -1 -0.045906218 1.732
2 2 1 1 -1 -0.045906218 1.732
2 2 -1 -1 1 -0.045906218 1.732
2 2 1 -1 1 -0.045906218 1.732
2 2 -1 1 1 -0.045906218 1.732
2 2 1 1 1 -0.045906218 1.732'''
input_uppasd = {
    'inpsd_ams':
    orm.Dict(
        dict={
            'simid':
            orm.Str('FeCo'),
            'ncell':
            orm.Str('20        20        20'),
            'BC':
            orm.Str('P         P         P '),
            'cell':
            orm.Str(
                """1.00000 0.00000 0.00000
                0.00000 1.00000 0.00000
                0.00000 0.00000 1.00000"""
            ),
            'Mensemble':
            orm.Int(1),
            'maptype':
            orm.Int(2),
            'SDEalgh':
            orm.Int(1),
            'Initmag':
            orm.Int(3),
            'ip_mode':
            orm.Str('M'),
            'ip_temp':
            orm.Int(100),
            'ip_mcNstep':
            orm.Int(5000),
            'qm_svec':
            orm.Str('1   -1   0 '),
            'qm_nvec':
            orm.Str('0  0  1'),
            'mode':
            orm.Str('S'),
            'temp':
            orm.Float(50),
            'damping':
            orm.Float(0.01),
            'Nstep':
            orm.Int(10000),
            'timestep':
            orm.Str('1.000e-16'),
            'qpoints':
            orm.Str('D'),
            'plotenergy':
            orm.Int(1),
            'do_avrg':
            orm.Str('Y'),
            'do_sc':
            orm.Str('Q'),
            'do_ams':
            orm.Str('Y'),
            'do_magdos':
            orm.Str('Y'),
            'do_sc_proj':
            orm.Str('Q'),
            'sc_step':
            orm.Int(20),
            'sc_nstep':
            orm.Int(5000),
            'magdos_freq':
            orm.Int(200),
            'magdos_sigma':
            orm.Int(30),
        }
    ),
    'num_machines':
    orm.Int(1),
    'num_mpiprocs_per_machine':
    orm.Int(16),
    'max_wallclock_seconds':
    orm.Int(2000),
    'code':
    orm.Code.get_from_string('uppasd_dev@uppasd_local'),
    'input_filename':
    orm.Str('inpsd.dat'),
    'parser_name':
    orm.Str('UppASD_core_parsers'),
    'label':
    orm.Str('uppasd_base_workflow_demo'),
    'description':
    orm.Str('Test base workflow'),
    'prepared_file_folder':
    orm.Str(os.path.join(os.getcwd(), 'AMS_input')),
    'except_filenames':
    orm.List(list=[]),
    'retrieve_list_name':
    orm.List(list=[('*', '.', 0), ('*.json', '.', 0)]),
    'J_model':
    orm.Int(2),
    'plot_dir':
    orm.Str(current_path),
    'AMSplot':
    orm.Bool('True'),
    'exchange_ams':
    orm.Dict(
        dict={
            '1': {
                'j_1': orm.Str(exchange_1),
            },
            '2': {
                'j_2': orm.Str(exchange_2),
            },
            '3': {
                'j_3': orm.Str(exchange_3),
            }
        }
    )
}

job_node = submit(UppASDMagnonSpectraRestartWorkflow, **input_uppasd)

print(f'UppASDAMSPlotWorkflow submitted, PK: {job_node.pk}')
with open('UppASDAMSPlotWorkflow_jobPK.csv', 'w') as f:
    f.write(str(job_node.pk))
