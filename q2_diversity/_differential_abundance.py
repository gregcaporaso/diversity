# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import biom
import qiime
import skbio.stats.composition

def ancom(output_dir: str, table: biom.Table,
          metadata: qiime.MetadataCategory) -> None:

    ancom_df, percentile_df = \
        skbio.stats.composition.ancom(table, metadata.to_series())

    with open(os.path.join(output_dir, 'index.html'), 'w') as fh:
        fh.write('<html><body>\n')
        fh.write('<h1>ANCOM test results</h1><br>')
        fh.write('%s<br>\n' % ancom_df.to_html())
        fh.write('<h1>Percentile abundances</h1><br>')
        fh.write('%s<br>\n' % percentile_df.to_html())
        fh.write('</body></html>')
