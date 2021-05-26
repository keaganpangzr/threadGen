import math
from lxml import etree



pitch_ratio = 1.07 #relative to major and minor dia
clearance = 0.15

data = f'''
<ThreadType>
  <Name>ThreadGen</Name>
  <CustomName>ThreadGen</CustomName>
  <Unit>mm</Unit>
  <Angle>95</Angle>
  <SortOrder>3</SortOrder>
  <ThreadForm>0</ThreadForm>
'''

for d in range(5,25):
    pitch = 3 if d < 10 else 5
    size = d

    ext_major = round(d*pitch_ratio,3)
    ext_pitch = d
    ext_minor = round(d/pitch_ratio,3)

    int_major = ext_major + clearance
    int_pitch = ext_pitch + clearance
    int_minor = ext_minor + clearance
    int_tap = d

    

    thread_data = f'''  <ThreadSize>
      <Size>{size}</Size>
      <Designation>
      <ThreadDesignation>M0.25x0.075</ThreadDesignation>
      <CTD>M0.25x0.075</CTD>
      <Pitch>{pitch}</Pitch>
      <Thread>
        <Gender>external</Gender>
        <Class>6g</Class>
        <MajorDia>{ext_major}</MajorDia>
        <PitchDia>{ext_pitch}</PitchDia>
        <MinorDia>{ext_minor}</MinorDia>
      </Thread>
      <Thread>
        <Gender>internal</Gender>
        <Class>6H</Class>
        <MajorDia>{int_major}</MajorDia>
        <PitchDia>{int_pitch}</PitchDia>
        <MinorDia>{int_minor}</MinorDia>
        <TapDrill>{int_tap}</TapDrill>
      </Thread>
      </Designation>
  </ThreadSize>
''' 
    data+= thread_data


data+= '</ThreadType>'



root = etree.fromstring(data)
et = etree.ElementTree(root)
et.write('ThreadGen.xml', pretty_print=True)