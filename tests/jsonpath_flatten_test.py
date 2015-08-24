#! /usr/bin/env python

import jsonpath_flatten, unittest

class TestJSONParse_Flatten (unittest.TestCase):

  def setUp (self):
    self.sample_dict = {
      "address": {
        "city": "New York",
        "postalCode": "10021",
        "state": "NY",
        "streetAddress": "21 2nd Street",
      },
      "age": 25,
      "firstName": "John",
      "lastName": "Smith",
      "phoneNumber": [
        {
          "number": "212 555-1234",
          "type": "home",
        },
        {
          "number": "646 555-4567",
          "type": "fax",
        },
      ],
      "uuid": "\xbf;\x9d[\xb4>L\x99\x95\r\x9e/\xfc2O2",
    }

  def test_base (self):
    reference_dict = {
      "address.city": "New York",
      "address.postalCode": "10021",
      "address.state": "NY",
      "address.streetAddress": "21 2nd Street",
      "age": 25,
      "firstName": "John",
      "lastName": "Smith",
      "phoneNumber.#count": 2,
      "phoneNumber[0].number": "212 555-1234",
      "phoneNumber[0].type": "home",
      "phoneNumber[1].number": "646 555-4567",
      "phoneNumber[1].type": "fax",
      "uuid": "bf3b9d5bb43e4c99950d9e2ffc324f32",
    }
    data = jsonpath_flatten.jsonpath_flatten (self.sample_dict)
    self.assertEqual (data, reference_dict)

if __name__ == "__main__":
  unittest.main()
