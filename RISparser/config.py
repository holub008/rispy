LIST_TYPE_TAGS = [
    'A1',
    'A2',
    'A3',
    'A4',
    'AU',
    'KW',
]

TAG_KEY_MAPPING = {
    'TY': "type_of_reference",
    'A1': "first_authors", #ListType
    'A2': "secondary_authors", #ListType
    'A3': "tertiary_authors", #ListType
    'A4': "subsidiary_authors", #ListType
    'AB': "abstract",
    'AD': "author_address",
    'AN': "accession_number",
    'AU': "authors", #ListType
    'C1': "custom1",
    'C2': "custom2",
    'C3': "custom3",
    'C4': "custom4",
    'C5': "custom5",
    'C6': "custom6",
    'C7': "custom7",
    'C8': "custom8",
    'CA': "caption",
    'CN': "call_number",
    'CY': "place_published",
    'DA': "date",
    'DB': "name_of_database",
    'DO': "doi",
    'DP': "database_provider",
    'ET': "edition",
    'EP': "end_page",
    'ID': "id",
    'IS': "number",
    'J2': "alternate_title1",
    'JA': "alternate_title2",
    'JF': "alternate_title3",
    'KW': "keywords", #ListType
    'L1': "file_attachments1",
    'L2': "file_attachments2",
    'L4': "figure",
    'LA': "language",
    'LB': "label",
    'M1': "note",
    'M3': "type_of_work",
    'N1': "notes",
    'N2': "abstract",
    'NV': "number_of_Volumes",
    'OP': "original_publication",
    'PB': "publisher",
    'PY': "year",
    'RI': "reviewed_item",
    'RN': "research_notes",
    'RP': "reprint_edition",
    'SE': "version",
    'SN': "issn",
    'SP': "start_page",
    'ST': "short_title",
    'T1': "primary_title",
    'T2': "secondary_title",
    'T3': "tertiary_title",
    'TA': "translated_author",
    'TI': "title",
    'TT': "translated_title",
    'UR': "url",
    'VL': "volume",
    'Y1': "publication_year",
    'Y2': "access_date",
    'ER': "end_of_reference"
}

TYPE_OF_REFERENCE_MAPPING = {
    'ABST': 'Abstract',
    'ADVS': 'Audiovisual material',
    'AGGR': 'Aggregated Database',
    'ANCIENT': 'Ancient Text',
    'ART': 'Art Work',
    'BILL': 'Bill',
    'BLOG': 'Blog',
    'BOOK': 'Whole book',
    'CASE': 'Case',
    'CHAP': 'Book chapter',
    'CHART': 'Chart',
    'CLSWK': 'Classical Work',
    'COMP': 'Computer program',
    'CONF': 'Conference proceeding',
    'CPAPER': 'Conference paper',
    'CTLG': 'Catalog',
    'DATA': 'Data file',
    'DBASE': 'Online Database',
    'DICT': 'Dictionary',
    'EBOOK': 'Electronic Book',
    'ECHAP': 'Electronic Book Section',
    'EDBOOK': 'Edited Book',
    'EJOUR': 'Electronic Article',
    'ELEC': 'Web Page',
    'ENCYC': 'Encyclopedia',
    'EQUA': 'Equation',
    'FIGURE': 'Figure',
    'GEN': 'Generic',
    'GOVDOC': 'Government Document',
    'GRANT': 'Grant',
    'HEAR': 'Hearing',
    'ICOMM': 'Internet Communication',
    'INPR': 'In Press',
    'JFULL': 'Journal (full)',
    'JOUR': 'Journal',
    'LEGAL': 'Legal Rule or Regulation',
    'MANSCPT': 'Manuscript',
    'MAP': 'Map',
    'MGZN': 'Magazine article',
    'MPCT': 'Motion picture',
    'MULTI': 'Online Multimedia',
    'MUSIC': 'Music score',
    'NEWS': 'Newspaper',
    'PAMP': 'Pamphlet',
    'PAT': 'Patent',
    'PCOMM': 'Personal communication',
    'RPRT': 'Report',
    'SER': 'Serial publication',
    'SLIDE': 'Slide',
    'SOUND': 'Sound recording',
    'STAND': 'Standard',
    'STAT': 'Statute',
    'THES': 'Thesis/Dissertation',
    'UNPB': 'Unpublished work',
    'VIDEO': 'Video recording',
}