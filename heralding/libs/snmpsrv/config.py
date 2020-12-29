DATA = {
  '1.3.6.1.4.1.1.1.0': integer(12345),
  '1.3.6.1.4.1.1.2.0': bit_string('\x12\x34\x56\x78'),
  '1.3.6.1.4.1.1.3.0': octet_string('test'),
  '1.3.6.1.4.1.1.4.0': null(),
  '1.3.6.1.4.1.1.5.0': object_identifier('1.3.6.7.8.9'),
  # notice the wildcards:
  '1.3.6.1.4.1.1.6.*': lambda oid: octet_string('* {}'.format(oid)),
  '1.3.6.1.4.1.1.?.0': lambda oid: octet_string('? {}'.format(oid)),
  '1.3.6.1.4.1.2.1.0': real(1.2345),
  '1.3.6.1.4.1.3.1.0': double(12345.2345),
}