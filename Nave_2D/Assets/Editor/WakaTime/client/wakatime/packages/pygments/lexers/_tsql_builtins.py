# -*- coding: utf-8 -*-
"""
    pygments.lexers._tsql_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    These are manually translated lists from https://msdn.microsoft.com.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# See https://msdn.microsoft.com/en-us/library/ms174986.aspx.
OPERATORS = (
    '!<',
    '!=',
    '!>',
    '<',
    '<=',
    '<>',
    '=',
    '>',
    '>=',
    '+',
    '+=',
    '-',
    '-=',
    '*',
    '*=',
    '/',
    '/=',
    '%',
    '%=',
    '&',
    '&=',
    '|',
    '|=',
    '^',
    '^=',
    '~',
    '::',
)

OPERATOR_WORDS = (
    'all',
    'and',
    'any',
    'between',
    'except',
    'exists',
    'in',
    'intersect',
    'like',
    'not',
    'or',
    'some',
    'union',
)

_KEYWORDS_SERVER = (
    'add',
    'all',
    'alter',
    'and',
    'any',
    'as',
    'asc',
    'authorization',
    'backup',
    'begin',
    'between',
    'break',
    'browse',
    'bulk',
    'by',
    'cascade',
    'case',
    'catch',
    'check',
    'checkpoint',
    'close',
    'clustered',
    'coalesce',
    'collate',
    'column',
    'commit',
    'compute',
    'constraint',
    'contains',
    'containstable',
    'continue',
    'convert',
    'create',
    'cross',
    'current',
    'current_date',
    'current_time',
    'current_timestamp',
    'current_user',
    'cursor',
    'database',
    'dbcc',
    'deallocate',
    'declare',
    'default',
    'delete',
    'deny',
    'desc',
    'disk',
    'distinct',
    'distributed',
    'double',
    'drop',
    'dump',
    'else',
    'end',
    'errlvl',
    'escape',
    'except',
    'exec',
    'execute',
    'exists',
    'exit',
    'external',
    'fetch',
    'file',
    'fillfactor',
    'for',
    'foreign',
    'freetext',
    'freetexttable',
    'from',
    'full',
    'function',
    'goto',
    'grant',
    'group',
    'having',
    'holdlock',
    'identity',
    'identity_insert',
    'identitycol',
    'if',
    'in',
    'index',
    'inner',
    'insert',
    'intersect',
    'into',
    'is',
    'join',
    'key',
    'kill',
    'left',
    'like',
    'lineno',
    'load',
    'merge',
    'national',
    'nocheck',
    'nonclustered',
    'not',
    'null',
    'nullif',
    'of',
    'off',
    'offsets',
    'on',
    'open',
    'opendatasource',
    'openquery',
    'openrowset',
    'openxml',
    'option',
    'or',
    'order',
    'outer',
    'over',
    'percent',
    'pivot',
    'plan',
    'precision',
    'primary',
    'print',
    'proc',
    'procedure',
    'public',
    'raiserror',
    'read',
    'readtext',
    'reconfigure',
    'references',
    'replication',
    'restore',
    'restrict',
    'return',
    'revert',
    'revoke',
    'right',
    'rollback',
    'rowcount',
    'rowguidcol',
    'rule',
    'save',
    'schema',
    'securityaudit',
    'select',
    'semantickeyphrasetable',
    'semanticsimilaritydetailstable',
    'semanticsimilaritytable',
    'session_user',
    'set',
    'setuser',
    'shutdown',
    'some',
    'statistics',
    'system_user',
    'table',
    'tablesample',
    'textsize',
    'then',
    'throw',
    'to',
    'top',
    'tran',
    'transaction',
    'trigger',
    'truncate',
    'try',
    'try_convert',
    'tsequal',
    'union',
    'unique',
    'unpivot',
    'update',
    'updatetext',
    'use',
    'user',
    'values',
    'varying',
    'view',
    'waitfor',
    'when',
    'where',
    'while',
    'with',
    'within',
    'writetext',
)

_KEYWORDS_FUTURE = (
    'absolute',
    'action',
    'admin',
    'after',
    'aggregate',
    'alias',
    'allocate',
    'are',
    'array',
    'asensitive',
    'assertion',
    'asymmetric',
    'at',
    'atomic',
    'before',
    'binary',
    'bit',
    'blob',
    'boolean',
    'both',
    'breadth',
    'call',
    'called',
    'cardinality',
    'cascaded',
    'cast',
    'catalog',
    'char',
    'character',
    'class',
    'clob',
    'collation',
    'collect',
    'completion',
    'condition',
    'connect',
    'connection',
    'constraints',
    'constructor',
    'corr',
    'corresponding',
    'covar_pop',
    'covar_samp',
    'cube',
    'cume_dist',
    'current_catalog',
    'current_default_transform_group',
    'current_path',
    'current_role',
    'current_schema',
    'current_transform_group_for_type',
    'cycle',
    'data',
    'date',
    'day',
    'dec',
    'decimal',
    'deferrable',
    'deferred',
    'depth',
    'deref',
    'describe',
    'descriptor',
    'destroy',
    'destructor',
    'deterministic',
    'diagnostics',
    'dictionary',
    'disconnect',
    'domain',
    'dynamic',
    'each',
    'element',
    'end-exec',
    'equals',
    'every',
    'exception',
    'false',
    'filter',
    'first',
    'float',
    'found',
    'free',
    'fulltexttable',
    'fusion',
    'general',
    'get',
    'global',
    'go',
    'grouping',
    'hold',
    'host',
    'hour',
    'ignore',
    'immediate',
    'indicator',
    'initialize',
    'initially',
    'inout',
    'input',
    'int',
    'integer',
    'intersection',
    'interval',
    'isolation',
    'iterate',
    'language',
    'large',
    'last',
    'lateral',
    'leading',
    'less',
    'level',
    'like_regex',
    'limit',
    'ln',
    'local',
    'localtime',
    'localtimestamp',
    'locator',
    'map',
    'match',
    'member',
    'method',
    'minute',
    'mod',
    'modifies',
    'modify',
    'module',
    'month',
    'multiset',
    'names',
    'natural',
    'nchar',
    'nclob',
    'new',
    'next',
    'no',
    'none',
    'normalize',
    'numeric',
    'object',
    'occurrences_regex',
    'old',
    'only',
    'operation',
    'ordinality',
    'out',
    'output',
    'overlay',
    'pad',
    'parameter',
    'parameters',
    'partial',
    'partition',
    'path',
    'percent_rank',
    'percentile_cont',
    'percentile_disc',
    'position_regex',
    'postfix',
    'prefix',
    'preorder',
    'prepare',
    'preserve',
    'prior',
    'privileges',
    'range',
    'reads',
    'real',
    'recursive',
    'ref',
    'referencing',
    'regr_avgx',
    'regr_avgy',
    'regr_count',
    'regr_intercept',
    'regr_r2',
    'regr_slope',
    'regr_sxx',
    'regr_sxy',
    'regr_syy',
    'relative',
    'release',
    'result',
    'returns',
    'role',
    'rollup',
    'routine',
    'row',
    'rows',
    'savepoint',
    'scope',
    'scroll',
    'search',
    'second',
    'section',
    'sensitive',
    'sequence',
    'session',
    'sets',
    'similar',
    'size',
    'smallint',
    'space',
    'specific',
    'specifictype',
    'sql',
    'sqlexception',
    'sqlstate',
    'sqlwarning',
    'start',
    'state',
    'statement',
    'static',
    'stddev_pop',
    'stddev_samp',
    'structure',
    'submultiset',
    'substring_regex',
    'symmetric',
    'system',
    'temporary',
    'terminate',
    'than',
    'time',
    'timestamp',
    'timezone_hour',
    'timezone_minute',
    'trailing',
    'translate_regex',
    'translation',
    'treat',
    'true',
    'uescape',
    'under',
    'unknown',
    'unnest',
    'usage',
    'using',
    'value',
    'var_pop',
    'var_samp',
    'varchar',
    'variable',
    'whenever',
    'width_bucket',
    'window',
    'within',
    'without',
    'work',
    'write',
    'xmlagg',
    'xmlattributes',
    'xmlbinary',
    'xmlcast',
    'xmlcomment',
    'xmlconcat',
    'xmldocument',
    'xmlelement',
    'xmlexists',
    'xmlforest',
    'xmliterate',
    'xmlnamespaces',
    'xmlparse',
    'xmlpi',
    'xmlquery',
    'xmlserialize',
    'xmltable',
    'xmltext',
    'xmlvalidate',
    'year',
    'zone',
)

_KEYWORDS_ODBC = (
    'absolute',
    'action',
    'ada',
    'add',
    'all',
    'allocate',
    'alter',
    'and',
    'any',
    'are',
    'as',
    'asc',
    'assertion',
    'at',
    'authorization',
    'avg',
    'begin',
    'between',
    'bit',
    'bit_length',
    'both',
    'by',
    'cascade',
    'cascaded',
    'case',
    'cast',
    'catalog',
    'char',
    'char_length',
    'character',
    'character_length',
    'check',
    'close',
    'coalesce',
    'collate',
    'collation',
    'column',
    'commit',
    'connect',
    'connection',
    'constraint',
    'constraints',
    'continue',
    'convert',
    'corresponding',
    'count',
    'create',
    'cross',
    'current',
    'current_date',
    'current_time',
    'current_timestamp',
    'current_user',
    'cursor',
    'date',
    'day',
    'deallocate',
    'dec',
    'decimal',
    'declare',
    'default',
    'deferrable',
    'deferred',
    'delete',
    'desc',
    'describe',
    'descriptor',
    'diagnostics',
    'disconnect',
    'distinct',
    'domain',
    'double',
    'drop',
    'else',
    'end',
    'end-exec',
    'escape',
    'except',
    'exception',
    'exec',
    'execute',
    'exists',
    'external',
    'extract',
    'false',
    'fetch',
    'first',
    'float',
    'for',
    'foreign',
    'fortran',
    'found',
    'from',
    'full',
    'get',
    'global',
    'go',
    'goto',
    'grant',
    'group',
    'having',
    'hour',
    'identity',
    'immediate',
    'in',
    'include',
    'index',
    'indicator',
    'initially',
    'inner',
    'input',
    'insensitive',
    'insert',
    'int',
    'integer',
    'intersect',
    'interval',
    'into',
    'is',
    'isolation',
    'join',
    'key',
    'language',
    'last',
    'leading',
    'left',
    'level',
    'like',
    'local',
    'lower',
    'match',
    'max',
    'min',
    'minute',
    'module',
    'month',
    'names',
    'national',
    'natural',
    'nchar',
    'next',
    'no',
    'none',
    'not',
    'null',
    'nullif',
    'numeric',
    'octet_length',
    'of',
    'on',
    'only',
    'open',
    'option',
    'or',
    'order',
    'outer',
    'output',
    'overlaps',
    'pad',
    'partial',
    'pascal',
    'position',
    'precision',
    'prepare',
    'preserve',
    'primary',
    'prior',
    'privileges',
    'procedure',
    'public',
    'read',
    'real',
    'references',
    'relative',
    'restrict',
    'revoke',
    'right',
    'rollback',
    'rows',
    'schema',
    'scroll',
    'second',
    'section',
    'select',
    'session',
    'session_user',
    'set',
    'size',
    'smallint',
    'some',
    'space',
    'sql',
    'sqlca',
    'sqlcode',
    'sqlerror',
    'sqlstate',
    'sqlwarning',
    'substring',
    'sum',
    'system_user',
    'table',
    'temporary',
    'then',
    'time',
    'timestamp',
    'timezone_hour',
    'timezone_minute',
    'to',
    'trailing',
    'transaction',
    'translate',
    'translation',
    'trim',
    'true',
    'union',
    'unique',
    'unknown',
    'update',
    'upper',
    'usage',
    'user',
    'using',
    'value',
    'values',
    'varchar',
    'varying',
    'view',
    'when',
    'whenever',
    'where',
    'with',
    'work',
    'write',
    'year',
    'zone',
)

# See https://msdn.microsoft.com/en-us/library/ms189822.aspx.
KEYWORDS = sorted(set(_KEYWORDS_FUTURE + _KEYWORDS_ODBC + _KEYWORDS_SERVER))

# See https://msdn.microsoft.com/en-us/library/ms187752.aspx.
TYPES = (
    'bigint',
    'binary',
    'bit',
    'char',
    'cursor',
    'date',
    'datetime',
    'datetime2',
    'datetimeoffset',
    'decimal',
    'float',
    'hierarchyid',
    'image',
    'int',
    'money',
    'nchar',
    'ntext',
    'numeric',
    'nvarchar',
    'real',
    'smalldatetime',
    'smallint',
    'smallmoney',
    'sql_variant',
    'table',
    'text',
    'time',
    'timestamp',
    'tinyint',
    'uniqueidentifier',
    'varbinary',
    'varchar',
    'xml',
)

# See https://msdn.microsoft.com/en-us/library/ms174318.aspx.
FUNCTIONS = (
    '$partition',
    'abs',
    'acos',
    'app_name',
    'applock_mode',
    'applock_test',
    'ascii',
    'asin',
    'assemblyproperty',
    'atan',
    'atn2',
    'avg',
    'binary_checksum',
    'cast',
    'ceiling',
    'certencoded',
    'certprivatekey',
    'char',
    'charindex',
    'checksum',
    'checksum_agg',
    'choose',
    'col_length',
    'col_name',
    'columnproperty',
    'compress',
    'concat',
    'connectionproperty',
    'context_info',
    'convert',
    'cos',
    'cot',
    'count',
    'count_big',
    'current_request_id',
    'current_timestamp',
    'current_transaction_id',
    'current_user',
    'cursor_status',
    'database_principal_id',
    'databasepropertyex',
    'dateadd',
    'datediff',
    'datediff_big',
    'datefromparts',
    'datename',
    'datepart',
    'datetime2fromparts',
    'datetimefromparts',
    'datetimeoffsetfromparts',
    'day',
    'db_id',
    'db_name',
    'decompress',
    'degrees',
    'dense_rank',
    'difference',
    'eomonth',
    'error_line',
    'error_message',
    'error_number',
    'error_procedure',
    'error_severity',
    'error_state',
    'exp',
    'file_id',
    'file_idex',
    'file_name',
    'filegroup_id',
    'filegroup_name',
    'filegroupproperty',
    'fileproperty',
    'floor',
    'format',
    'formatmessage',
    'fulltextcatalogproperty',
    'fulltextserviceproperty',
    'get_filestream_transaction_context',
    'getansinull',
    'getdate',
    'getutcdate',
    'grouping',
    'grouping_id',
    'has_perms_by_name',
    'host_id',
    'host_name',
    'iif',
    'index_col',
    'indexkey_property',
    'indexproperty',
    'is_member',
    'is_rolemember',
    'is_srvrolemember',
    'isdate',
    'isjson',
    'isnull',
    'isnumeric',
    'json_modify',
    'json_query',
    'json_value',
    'left',
    'len',
    'log',
    'log10',
    'lower',
    'ltrim',
    'max',
    'min',
    'min_active_rowversion',
    'month',
    'nchar',
    'newid',
    'newsequentialid',
    'ntile',
    'object_definition',
    'object_id',
    'object_name',
    'object_schema_name',
    'objectproperty',
    'objectpropertyex',
    'opendatasource',
    'openjson',
    'openquery',
    'openrowset',
    'openxml',
    'original_db_name',
    'original_login',
    'parse',
    'parsename',
    'patindex',
    'permissions',
    'pi',
    'power',
    'pwdcompare',
    'pwdencrypt',
    'quotename',
    'radians',
    'rand',
    'rank',
    'replace',
    'replicate',
    'reverse',
    'right',
    'round',
    'row_number',
    'rowcount_big',
    'rtrim',
    'schema_id',
    'schema_name',
    'scope_identity',
    'serverproperty',
    'session_context',
    'session_user',
    'sign',
    'sin',
    'smalldatetimefromparts',
    'soundex',
    'sp_helplanguage',
    'space',
    'sqrt',
    'square',
    'stats_date',
    'stdev',
    'stdevp',
    'str',
    'string_escape',
    'string_split',
    'stuff',
    'substring',
    'sum',
    'suser_id',
    'suser_name',
    'suser_sid',
    'suser_sname',
    'switchoffset',
    'sysdatetime',
    'sysdatetimeoffset',
    'system_user',
    'sysutcdatetime',
    'tan',
    'textptr',
    'textvalid',
    'timefromparts',
    'todatetimeoffset',
    'try_cast',
    'try_convert',
    'try_parse',
    'type_id',
    'type_name',
    'typeproperty',
    'unicode',
    'upper',
    'user_id',
    'user_name',
    'var',
    'varp',
    'xact_state',
    'year',
)
