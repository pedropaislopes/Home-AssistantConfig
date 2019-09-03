d = { '5E170A':['janela_cozinha'     ,'ON' ,'true'],
      '5E170E':['janela_cozinha'     ,'OFF','true'],
      '5BEC0A':['janela_aservico'    ,'ON' ,'true'],
      '5BEC0E':['janela_aservico'    ,'OFF','true'],
      '5A9D0A':['janela_escritorio'  ,'ON' ,'true'],
      '5A9D0E':['janela_escritorio'  ,'OFF','true'],
      '59C80A':['janela_quartolorena','ON' ,'true'],
      '59C80E':['janela_quartolorena','OFF','true'],
      '5C9C0A':['janela_suite'       ,'ON' ,'true'],
      '5C9C0E':['janela_suite'       ,'OFF','true']
    }

p = data.get('payload')

if p is not None:
  if p in d.keys():
    service_data = {'topic':'home/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':0, 'retain':'{}'.format(d[p][2])}
  else:
    service_data = {'topic':'home/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
  hass.services.call('mqtt', 'publish', service_data, False)
