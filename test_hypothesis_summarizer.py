import unittest
import json
import io
#from sp_summarizer import (SpacyTsSummarizer)
from ts_summarizer import (TextRankTsSummarizer)
from interval_summarizer import (IntervalSpec, TsSummarizer, tagged_sum,
                                 ts_to_time)
from datetime import datetime
import logging
import sys
import config
from ts_config import DEBUG
from hypothesis import given
#import hypothesis.strategies as st
from hypothesis.strategies import (sampled_from, lists, just, integers)
import glob

logger = logging.getLogger()
logger.level = logging.DEBUG if DEBUG else logging.INFO
test_json_msgs = json.load(io.open("./test-events.json", encoding='utf-8'))['messages']
test_json_msgs_c2 = json.load(io.open("./data/test-events-elastic.json", encoding='utf-8'))['messages']
test_json_msgs_c3 = []
for jfile in glob.glob('./data/slack-logs-2/jetpack/*.json'):
    test_json_msgs_c3 += json.load(io.open(jfile, encoding='utf-8'))

print len(test_json_msgs_c3)

class TestSummarize(unittest.TestCase):

    test_msgs = test_json_msgs

    @given(
        lists(elements=sampled_from(test_json_msgs), min_size=1),
        integers(min_value=1, max_value=20)
    )
    def test_text_rank_summarization_ds1_days(self, smp_msgs, days):
        """Generate something for N day interval"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'days': days, 'size' : 3, 'txt' : u'Summary for first {} days:\n'.format(days)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message


    @given(
        lists(elements=sampled_from(test_json_msgs_c2), min_size=1),
        integers(min_value=1, max_value=20)
    )
    def test_text_rank_summarization_ds2_days(self, smp_msgs, days):
        """Generate something for N day interval"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'days': days, 'size' : 3, 'txt' : u'Summary for first {} days:\n'.format(days)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message


    @given(
        lists(elements=sampled_from(test_json_msgs_c3), min_size=1),
        integers(min_value=1, max_value=20)
    )
    def test_text_rank_summarization_ds3_days(self, smp_msgs, days):
        """Generate something for N day interval"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'days': days, 'size' : 3, 'txt' : u'Summary for first {} days:\n'.format(days)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message


    @given(lists(elements=sampled_from(test_json_msgs), min_size=1),
           integers(min_value=1, max_value=24)
    )
    def test_text_rank_summarization_ds1_hours(self, smp_msgs, hours):
        """Generate something for N hour intervals"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'hours': hours, 'size' : 3, 'txt' : u'Summary for first {} minutes:\n'.format(hours)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message
        

    @given(lists(elements=sampled_from(test_json_msgs_c2), min_size=1),
           integers(min_value=1, max_value=24)
    )
    def test_text_rank_summarization_ds2_hours(self, smp_msgs, hours):
        """Generate something for N hour intervals"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'hours': hours, 'size' : 3, 'txt' : u'Summary for first {} minutes:\n'.format(hours)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message
        

    @given(lists(elements=sampled_from(test_json_msgs_c3), min_size=1),
           integers(min_value=1, max_value=24)
    )
    def test_text_rank_summarization_ds3_hours(self, smp_msgs, hours):
        """Generate something for N hour intervals"""
        logger.info("Input is %s", smp_msgs)
        asd = [{'hours': hours, 'size' : 3, 'txt' : u'Summary for first {} minutes:\n'.format(hours)}]
        summ = TextRankTsSummarizer(asd)
        sumry = summ.summarize(smp_msgs)
        logger.debug("Summary is %s", sumry)
        # Length of summary is at least 1 and no greater than 3
        self.assertTrue(len(sumry) >= 1)
        self.assertTrue(len(sumry) <= 3)
        # Length of summary is less than or equal to the original length
        self.assertTrue(len(sumry) <= len(smp_msgs))
        # Each message in the summary must correspond to a message
        

if __name__ == '__main__':
    unittest.main()

