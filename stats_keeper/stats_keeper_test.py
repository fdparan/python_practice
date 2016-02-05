'''
Created on Oct 25, 2015

@author: francisparan
'''
import unittest

import stats_keeper


class Test(unittest.TestCase):

    def setUp(self):
        self.club_obj = stats_keeper.Club('My Club FC')
        self.stat_obj = stats_keeper.GoalStatistics()
        
    def tearDown(self):
        del self.club_obj
        del self.stat_obj
    
    def testClubExists(self):
        self.assertTrue(self.club_obj)
        
    def testClubNotExistsOnException(self):
        
        with self.assertRaises(TypeError):
            obj = stats_keeper.Club([])
        
            self.assertIsNone(obj)

    def testAddGoal(self):        
        self.makeAssertionOnGoalStats(self.stat_obj.add_stat_point, 'self.stat_obj.goals_for')
        
    def testConcedeGoal(self):
        self.makeAssertionOnGoalStats(self.stat_obj.lose_stat_point, 'self.stat_obj.goals_against')
    
    def makeAssertionOnGoalStats(self, func, stat):
        
        #this should add nothing to the stat, upon passing a non-int type
        func(None)
        self.assertEquals(eval(stat), 0)
        
        stat_points = 0
        
        while stat_points < 5:
            func()
            stat_points += 1
        
        # goals made: 5
        self.assertEquals(eval(stat), stat_points)
        
        # goals made: 5 + 3 = 8
        func(3)
        self.assertEquals(eval(stat), 8)
        
        # goals made: 5 + 1 = 6
        func(-2)
        self.assertEquals(eval(stat), 6)
        
        # value should still be the same as the previous one above
        func([])
        self.assertEquals(eval(stat), 6)
        
    def test_goal_difference(self):
        gameSheet = stats_keeper.SoccerGameSheet(self.club_obj)
        self.assertIsInstance(gameSheet.goal_difference(), int)       
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()