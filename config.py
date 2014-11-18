replace = {
    '.svg':'.png',
    # windows
    'file://':'http://localhost',
    # linux
    #'xlink:href="':'xlink:href="http://localhost/',
    '<se:Format>image/svg+xml</se:Format>':'<se:Format>image/png</se:Format>',
    '<se:WellKnownName>x</se:WellKnownName>':'<se:WellKnownName>shape://times</se:WellKnownName>',
    '<se:WellKnownName>cross</se:WellKnownName>':'<se:WellKnownName>shape://plus</se:WellKnownName>',
    '<se:WellKnownName>line</se:WellKnownName>':'<se:WellKnownName>shape://vertline</se:WellKnownName>',
    '<se:WellKnownName>horline</se:WellKnownName>':'<se:WellKnownName>shape://horline</se:WellKnownName>',
    '<se:WellKnownName>slash</se:WellKnownName>':'<se:WellKnownName>shape://slash</se:WellKnownName>',
    '<se:WellKnownName>backslash</se:WellKnownName>':'<se:WellKnownName>shape://backslash</se:WellKnownName>'
}

params = {
    'post-url':'http://localhost:8080/kaartenbalie/files',
    'post-username':'beheerder',
    'post-password':'beheerder',
    'post-workspace-param':'filename',
    'default-workspace':'b3p',
    'stroke-width-multiplier':3,
    'point-size-multiplier':8
}
