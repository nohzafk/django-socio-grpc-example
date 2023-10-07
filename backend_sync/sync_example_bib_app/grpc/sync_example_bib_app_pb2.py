# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sync_example_bib_app/grpc/sync_example_bib_app.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4sync_example_bib_app/grpc/sync_example_bib_app.proto\x12 dsg_example.sync_example_bib_app\x1a\x1bgoogle/protobuf/empty.proto\")\n\x14\x41uthorDestroyRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\"\x13\n\x11\x41uthorListRequest\"W\n\x12\x41uthorListResponse\x12\x41\n\x07results\x18\x01 \x03(\x0b\x32\x30.dsg_example.sync_example_bib_app.AuthorResponse\"\x8a\x01\n\x1a\x41uthorPartialUpdateRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x12\n\nname_first\x18\x02 \x01(\t\x12\x11\n\tname_last\x18\x03 \x01(\t\x12\x12\n\nbirth_date\x18\x04 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x05 \x03(\t\"]\n\rAuthorRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x12\n\nname_first\x18\x02 \x01(\t\x12\x11\n\tname_last\x18\x03 \x01(\t\x12\x12\n\nbirth_date\x18\x04 \x01(\t\"^\n\x0e\x41uthorResponse\x12\x11\n\tauthor_id\x18\x01 \x01(\t\x12\x12\n\nname_first\x18\x02 \x01(\t\x12\x11\n\tname_last\x18\x03 \x01(\t\x12\x12\n\nbirth_date\x18\x04 \x01(\t\"*\n\x15\x41uthorRetrieveRequest\x12\x11\n\tauthor_id\x18\x01 \x01(\t\"%\n\x12\x42ookDestroyRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\"\x11\n\x0f\x42ookListRequest\"S\n\x10\x42ookListResponse\x12?\n\x07results\x18\x01 \x03(\x0b\x32..dsg_example.sync_example_bib_app.BookResponse\"\xba\x01\n\x18\x42ookPartialUpdateRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x0c\n\x04isbn\x18\x05 \x01(\t\x12\x11\n\tpublisher\x18\x06 \x01(\t\x12\x18\n\x10publication_date\x18\x07 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x08 \x03(\t\"\x8d\x01\n\x0b\x42ookRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x0c\n\x04isbn\x18\x05 \x01(\t\x12\x11\n\tpublisher\x18\x06 \x01(\t\x12\x18\n\x10publication_date\x18\x07 \x01(\t\"\x8e\x01\n\x0c\x42ookResponse\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x0c\n\x04isbn\x18\x05 \x01(\t\x12\x11\n\tpublisher\x18\x06 \x01(\t\x12\x18\n\x10publication_date\x18\x07 \x01(\t\"&\n\x13\x42ookRetrieveRequest\x12\x0f\n\x07\x62ook_id\x18\x01 \x01(\t\"+\n\x15JournalDestroyRequest\x12\x12\n\njournal_id\x18\x01 \x01(\t\"\x14\n\x12JournalListRequest\"Y\n\x13JournalListResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.dsg_example.sync_example_bib_app.JournalResponse\"\xdf\x01\n\x1bJournalPartialUpdateRequest\x12\x12\n\njournal_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x11\n\tpublisher\x18\x05 \x01(\t\x12\x18\n\x10publication_date\x18\x06 \x01(\t\x12\x0e\n\x06volume\x18\x07 \x01(\x05\x12\r\n\x05issue\x18\x08 \x01(\x05\x12\x0c\n\x04issn\x18\t \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\n \x03(\t\"\xb2\x01\n\x0eJournalRequest\x12\x12\n\njournal_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x11\n\tpublisher\x18\x05 \x01(\t\x12\x18\n\x10publication_date\x18\x06 \x01(\t\x12\x0e\n\x06volume\x18\x07 \x01(\x05\x12\r\n\x05issue\x18\x08 \x01(\x05\x12\x0c\n\x04issn\x18\t \x01(\t\"\xb3\x01\n\x0fJournalResponse\x12\x12\n\njournal_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x03 \x03(\t\x12\x12\n\ncategories\x18\x04 \x03(\t\x12\x11\n\tpublisher\x18\x05 \x01(\t\x12\x18\n\x10publication_date\x18\x06 \x01(\t\x12\x0e\n\x06volume\x18\x07 \x01(\x05\x12\r\n\x05issue\x18\x08 \x01(\x05\x12\x0c\n\x04issn\x18\t \x01(\t\",\n\x16JournalRetrieveRequest\x12\x12\n\njournal_id\x18\x01 \x01(\t\"8\n!PublicationCategoryDestroyRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\" \n\x1ePublicationCategoryListRequest\"q\n\x1fPublicationCategoryListResponse\x12N\n\x07results\x18\x01 \x03(\x0b\x32=.dsg_example.sync_example_bib_app.PublicationCategoryResponse\"l\n\'PublicationCategoryPartialUpdateRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x03 \x03(\t\"?\n\x1aPublicationCategoryRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"@\n\x1bPublicationCategoryResponse\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"9\n\"PublicationCategoryRetrieveRequest\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\"/\n\x17PublisherDestroyRequest\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t\"\x16\n\x14PublisherListRequest\"]\n\x15PublisherListResponse\x12\x44\n\x07results\x18\x01 \x03(\x0b\x32\x33.dsg_example.sync_example_bib_app.PublisherResponse\"\xbc\x01\n\x1dPublisherPartialUpdateRequest\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x16\n\x0estate_province\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0f\n\x07website\x18\x07 \x01(\t\x12\x1e\n\x16_partial_update_fields\x18\x08 \x03(\t\"\x8f\x01\n\x10PublisherRequest\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x16\n\x0estate_province\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0f\n\x07website\x18\x07 \x01(\t\"\x90\x01\n\x11PublisherResponse\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04\x63ity\x18\x04 \x01(\t\x12\x16\n\x0estate_province\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0f\n\x07website\x18\x07 \x01(\t\"0\n\x18PublisherRetrieveRequest\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\t2\xbf\x05\n\x10\x41uthorController\x12m\n\x06\x43reate\x12/.dsg_example.sync_example_bib_app.AuthorRequest\x1a\x30.dsg_example.sync_example_bib_app.AuthorResponse\"\x00\x12[\n\x07\x44\x65stroy\x12\x36.dsg_example.sync_example_bib_app.AuthorDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12s\n\x04List\x12\x33.dsg_example.sync_example_bib_app.AuthorListRequest\x1a\x34.dsg_example.sync_example_bib_app.AuthorListResponse\"\x00\x12\x81\x01\n\rPartialUpdate\x12<.dsg_example.sync_example_bib_app.AuthorPartialUpdateRequest\x1a\x30.dsg_example.sync_example_bib_app.AuthorResponse\"\x00\x12w\n\x08Retrieve\x12\x37.dsg_example.sync_example_bib_app.AuthorRetrieveRequest\x1a\x30.dsg_example.sync_example_bib_app.AuthorResponse\"\x00\x12m\n\x06Update\x12/.dsg_example.sync_example_bib_app.AuthorRequest\x1a\x30.dsg_example.sync_example_bib_app.AuthorResponse\"\x00\x32\xa6\x05\n\x0e\x42ookController\x12i\n\x06\x43reate\x12-.dsg_example.sync_example_bib_app.BookRequest\x1a..dsg_example.sync_example_bib_app.BookResponse\"\x00\x12Y\n\x07\x44\x65stroy\x12\x34.dsg_example.sync_example_bib_app.BookDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12o\n\x04List\x12\x31.dsg_example.sync_example_bib_app.BookListRequest\x1a\x32.dsg_example.sync_example_bib_app.BookListResponse\"\x00\x12}\n\rPartialUpdate\x12:.dsg_example.sync_example_bib_app.BookPartialUpdateRequest\x1a..dsg_example.sync_example_bib_app.BookResponse\"\x00\x12s\n\x08Retrieve\x12\x35.dsg_example.sync_example_bib_app.BookRetrieveRequest\x1a..dsg_example.sync_example_bib_app.BookResponse\"\x00\x12i\n\x06Update\x12-.dsg_example.sync_example_bib_app.BookRequest\x1a..dsg_example.sync_example_bib_app.BookResponse\"\x00\x32\xcb\x05\n\x11JournalController\x12o\n\x06\x43reate\x12\x30.dsg_example.sync_example_bib_app.JournalRequest\x1a\x31.dsg_example.sync_example_bib_app.JournalResponse\"\x00\x12\\\n\x07\x44\x65stroy\x12\x37.dsg_example.sync_example_bib_app.JournalDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12u\n\x04List\x12\x34.dsg_example.sync_example_bib_app.JournalListRequest\x1a\x35.dsg_example.sync_example_bib_app.JournalListResponse\"\x00\x12\x83\x01\n\rPartialUpdate\x12=.dsg_example.sync_example_bib_app.JournalPartialUpdateRequest\x1a\x31.dsg_example.sync_example_bib_app.JournalResponse\"\x00\x12y\n\x08Retrieve\x12\x38.dsg_example.sync_example_bib_app.JournalRetrieveRequest\x1a\x31.dsg_example.sync_example_bib_app.JournalResponse\"\x00\x12o\n\x06Update\x12\x30.dsg_example.sync_example_bib_app.JournalRequest\x1a\x31.dsg_example.sync_example_bib_app.JournalResponse\"\x00\x32\xdf\x06\n\x1dPublicationCategoryController\x12\x87\x01\n\x06\x43reate\x12<.dsg_example.sync_example_bib_app.PublicationCategoryRequest\x1a=.dsg_example.sync_example_bib_app.PublicationCategoryResponse\"\x00\x12h\n\x07\x44\x65stroy\x12\x43.dsg_example.sync_example_bib_app.PublicationCategoryDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x8d\x01\n\x04List\x12@.dsg_example.sync_example_bib_app.PublicationCategoryListRequest\x1a\x41.dsg_example.sync_example_bib_app.PublicationCategoryListResponse\"\x00\x12\x9b\x01\n\rPartialUpdate\x12I.dsg_example.sync_example_bib_app.PublicationCategoryPartialUpdateRequest\x1a=.dsg_example.sync_example_bib_app.PublicationCategoryResponse\"\x00\x12\x91\x01\n\x08Retrieve\x12\x44.dsg_example.sync_example_bib_app.PublicationCategoryRetrieveRequest\x1a=.dsg_example.sync_example_bib_app.PublicationCategoryResponse\"\x00\x12\x87\x01\n\x06Update\x12<.dsg_example.sync_example_bib_app.PublicationCategoryRequest\x1a=.dsg_example.sync_example_bib_app.PublicationCategoryResponse\"\x00\x32\xe3\x05\n\x13PublisherController\x12s\n\x06\x43reate\x12\x32.dsg_example.sync_example_bib_app.PublisherRequest\x1a\x33.dsg_example.sync_example_bib_app.PublisherResponse\"\x00\x12^\n\x07\x44\x65stroy\x12\x39.dsg_example.sync_example_bib_app.PublisherDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12y\n\x04List\x12\x36.dsg_example.sync_example_bib_app.PublisherListRequest\x1a\x37.dsg_example.sync_example_bib_app.PublisherListResponse\"\x00\x12\x87\x01\n\rPartialUpdate\x12?.dsg_example.sync_example_bib_app.PublisherPartialUpdateRequest\x1a\x33.dsg_example.sync_example_bib_app.PublisherResponse\"\x00\x12}\n\x08Retrieve\x12:.dsg_example.sync_example_bib_app.PublisherRetrieveRequest\x1a\x33.dsg_example.sync_example_bib_app.PublisherResponse\"\x00\x12s\n\x06Update\x12\x32.dsg_example.sync_example_bib_app.PublisherRequest\x1a\x33.dsg_example.sync_example_bib_app.PublisherResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sync_example_bib_app.grpc.sync_example_bib_app_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTHORDESTROYREQUEST._serialized_start=119
  _AUTHORDESTROYREQUEST._serialized_end=160
  _AUTHORLISTREQUEST._serialized_start=162
  _AUTHORLISTREQUEST._serialized_end=181
  _AUTHORLISTRESPONSE._serialized_start=183
  _AUTHORLISTRESPONSE._serialized_end=270
  _AUTHORPARTIALUPDATEREQUEST._serialized_start=273
  _AUTHORPARTIALUPDATEREQUEST._serialized_end=411
  _AUTHORREQUEST._serialized_start=413
  _AUTHORREQUEST._serialized_end=506
  _AUTHORRESPONSE._serialized_start=508
  _AUTHORRESPONSE._serialized_end=602
  _AUTHORRETRIEVEREQUEST._serialized_start=604
  _AUTHORRETRIEVEREQUEST._serialized_end=646
  _BOOKDESTROYREQUEST._serialized_start=648
  _BOOKDESTROYREQUEST._serialized_end=685
  _BOOKLISTREQUEST._serialized_start=687
  _BOOKLISTREQUEST._serialized_end=704
  _BOOKLISTRESPONSE._serialized_start=706
  _BOOKLISTRESPONSE._serialized_end=789
  _BOOKPARTIALUPDATEREQUEST._serialized_start=792
  _BOOKPARTIALUPDATEREQUEST._serialized_end=978
  _BOOKREQUEST._serialized_start=981
  _BOOKREQUEST._serialized_end=1122
  _BOOKRESPONSE._serialized_start=1125
  _BOOKRESPONSE._serialized_end=1267
  _BOOKRETRIEVEREQUEST._serialized_start=1269
  _BOOKRETRIEVEREQUEST._serialized_end=1307
  _JOURNALDESTROYREQUEST._serialized_start=1309
  _JOURNALDESTROYREQUEST._serialized_end=1352
  _JOURNALLISTREQUEST._serialized_start=1354
  _JOURNALLISTREQUEST._serialized_end=1374
  _JOURNALLISTRESPONSE._serialized_start=1376
  _JOURNALLISTRESPONSE._serialized_end=1465
  _JOURNALPARTIALUPDATEREQUEST._serialized_start=1468
  _JOURNALPARTIALUPDATEREQUEST._serialized_end=1691
  _JOURNALREQUEST._serialized_start=1694
  _JOURNALREQUEST._serialized_end=1872
  _JOURNALRESPONSE._serialized_start=1875
  _JOURNALRESPONSE._serialized_end=2054
  _JOURNALRETRIEVEREQUEST._serialized_start=2056
  _JOURNALRETRIEVEREQUEST._serialized_end=2100
  _PUBLICATIONCATEGORYDESTROYREQUEST._serialized_start=2102
  _PUBLICATIONCATEGORYDESTROYREQUEST._serialized_end=2158
  _PUBLICATIONCATEGORYLISTREQUEST._serialized_start=2160
  _PUBLICATIONCATEGORYLISTREQUEST._serialized_end=2192
  _PUBLICATIONCATEGORYLISTRESPONSE._serialized_start=2194
  _PUBLICATIONCATEGORYLISTRESPONSE._serialized_end=2307
  _PUBLICATIONCATEGORYPARTIALUPDATEREQUEST._serialized_start=2309
  _PUBLICATIONCATEGORYPARTIALUPDATEREQUEST._serialized_end=2417
  _PUBLICATIONCATEGORYREQUEST._serialized_start=2419
  _PUBLICATIONCATEGORYREQUEST._serialized_end=2482
  _PUBLICATIONCATEGORYRESPONSE._serialized_start=2484
  _PUBLICATIONCATEGORYRESPONSE._serialized_end=2548
  _PUBLICATIONCATEGORYRETRIEVEREQUEST._serialized_start=2550
  _PUBLICATIONCATEGORYRETRIEVEREQUEST._serialized_end=2607
  _PUBLISHERDESTROYREQUEST._serialized_start=2609
  _PUBLISHERDESTROYREQUEST._serialized_end=2656
  _PUBLISHERLISTREQUEST._serialized_start=2658
  _PUBLISHERLISTREQUEST._serialized_end=2680
  _PUBLISHERLISTRESPONSE._serialized_start=2682
  _PUBLISHERLISTRESPONSE._serialized_end=2775
  _PUBLISHERPARTIALUPDATEREQUEST._serialized_start=2778
  _PUBLISHERPARTIALUPDATEREQUEST._serialized_end=2966
  _PUBLISHERREQUEST._serialized_start=2969
  _PUBLISHERREQUEST._serialized_end=3112
  _PUBLISHERRESPONSE._serialized_start=3115
  _PUBLISHERRESPONSE._serialized_end=3259
  _PUBLISHERRETRIEVEREQUEST._serialized_start=3261
  _PUBLISHERRETRIEVEREQUEST._serialized_end=3309
  _AUTHORCONTROLLER._serialized_start=3312
  _AUTHORCONTROLLER._serialized_end=4015
  _BOOKCONTROLLER._serialized_start=4018
  _BOOKCONTROLLER._serialized_end=4696
  _JOURNALCONTROLLER._serialized_start=4699
  _JOURNALCONTROLLER._serialized_end=5414
  _PUBLICATIONCATEGORYCONTROLLER._serialized_start=5417
  _PUBLICATIONCATEGORYCONTROLLER._serialized_end=6280
  _PUBLISHERCONTROLLER._serialized_start=6283
  _PUBLISHERCONTROLLER._serialized_end=7022
# @@protoc_insertion_point(module_scope)
