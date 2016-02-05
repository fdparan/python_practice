'''
Created on Oct 24, 2015

@author: francisparan
'''

import datetime
from pprint import pprint


#TODO: Don't know what to do with these classes yet, stay tuned.....

class Table:
    def __init__(self, name = ''):
        self.name = name
    
    def show_table(self):
        print('Showing "{}" table'.format(self.name))

class SoccerTable(Table):
    
    def __init__(self, name, clubs):
        Table.__init__(self, name)
        
        self.clubs = clubs
        
class League(object):
    
    def __init__(self, name, clubs):
        self.name = name
        self.clubs = clubs
        self.standing = []
        
    def start_season(self):
        for club in self.clubs:
            points, goals_for, goals_against = 0
            row = club, points, goals_for, goals_against
            
            self.standing.append(row)
            
    def show_table(self):
        pprint(self.standing)    

# This is the used code.

class Statistics(object):
    
    def __str__(self):
        return ''
    
    def _add_new_value(self, point):
        return point if isinstance(point, int) else 0
    
    def add_stat_point(self, points = 1):
        pass
    
    def lose_stat_point(self, points = 1):
        pass
    
class GoalStatistics(Statistics):
    
    def __init__(self):
        self.goals_for = 0
        self.goals_against = 0
              
    def add_stat_point(self, points = 1):
        self.goals_for += self._add_new_value(points)
        
    def lose_stat_point(self, points = 1):
        self.goals_against += self._add_new_value(points)
        
    def __str__(self):
        return '''
            %d goals for
            %d goals against
            %d goal difference
        ''' % (self.goals_for, self.goals_against, self.goals_for-self.goals_against)

class ShotStatistics(Statistics):
    def __init__(self):
        self.shot_attempts = 0
        self.shots_on_target = 0
        self.shots_off_target = 0
        
    def add_shot_on_target(self, shots = 1):
        self.shot_attempts += self._add_new_value(shots)
        self.shots_on_target += self._add_new_value(shots)

    def add_shot_off_target(self, shots = 1):
        self.shot_attempts += self._add_new_value(shots)
        self.shots_off_target += self._add_new_value(shots)
        
    def __str__(self):
        return '''
            %d shot attempts
            %d shots on target
            %d shots off target
        ''' % (self.shot_attempts, self.shots_on_target, self.shots_off_target)

class StatRecord(object):
    def __init__(self, club, date):
        club.add_stat(self, date)
        self.stats = {}

class SoccerStatRecord(StatRecord):
    def __init__(self, club, date):
        super(SoccerStatRecord, self).__init__(club, date)
        self.stats.update(samp(goals = GoalStatistics(), shots = ShotStatistics()))
        self.points = 0
        
class Club:
    def __init__(self, name = None):
        
        try:
            if not isinstance(name, str):
                raise TypeError('Error: Name must be a string (name = %s).' % name)
            self.name = name
            self.stats = {}
            
        except TypeError as e:
            print e
            raise
        
    def add_stat(self, stat, date):
        self.stats[date] = stat

    def get_recorded_stats(self, date = ''):
        
        if not date:
            return ''
        
        return '''
        %s Statistics for %s:
            %s
        ''' % (date, self.name, self.stats.get(date, ''))
        
    def __str__(self):
        return self.name

class SoccerGameSheet:
    
    def __init__(self, club, date = datetime.date.today()):
        self.club = club
        self.date = date
        
        self.club.add_stat(GoalStatistics(), str(self.date))
        
        self.points = 0
        
    def add_stat_point(self, points = 1):
        self.points += points if isinstance(points, int) else 0
        
    def goal_difference(self):
        return self.get_goal_stats().goals_for - self.get_goal_stats().goals_against
    
    def get_goal_stats(self):
        return self.club.stats.get(str(self.date), None)
    
    def __str__(self):
        return '''%s
            %d points
            %d goal difference
            
            %s'''%(self.club, self.points, self.goal_difference(), self.get_goal_stats())
    
class Match:
    def __init__(self, home_game_sheet, opp_game_sheet):
        self.home_game_sheet = home_game_sheet
        self.score_home = self.score_opp = 0
        self.opp_game_sheet = opp_game_sheet
        
    def goal_home(self, player, goal_minute):
        self.score_home += 1
        
        self.announce(self.show_score())
        self.goal_announce(player, self.home_game_sheet.club, goal_minute)
        
        self.home_game_sheet.get_goal_stats().add_stat_point()
        self.opp_game_sheet.get_goal_stats().lose_stat_point()
        
    def goal_opp(self, player, goal_minute):
        self.score_opp += 1
        
        self.announce(self.show_score())
        self.goal_announce(player, self.opp_game_sheet.club, goal_minute)
        
        self.opp_game_sheet.get_goal_stats().add_stat_point()
        self.home_game_sheet.get_goal_stats().lose_stat_point()
        
    def announce(self, msg, header = '='):
        
        print('\n'+ header*len(msg))
        print(msg)
        print(header*len(msg))

    def goal_announce(self, player, club, goal_minute):
        self.announce(
          '%s for %s has made a goal in the %d minute.' % (player, club, goal_minute),
          '-')
        
    def show_score(self):
        return '%s %d - %d %s' % (self.home_game_sheet.club, self.score_home, self.score_opp, self.opp_game_sheet.club)
    
    
    def halftime(self):
        self.announce('Halftime: %s' % self.show_score())
           
    def final_score(self):
        self.announce('Final Score: %s' % self.show_score())
        
        self.allocate_points()
        
    def allocate_points(self):
        
        if self.score_home > self.score_opp:
            self.home_game_sheet.add_stat_point(3)
        elif self.score_opp > self.score_home:
            self.opp_game_sheet.add_stat_point(3)
        else:
            self.home_game_sheet.add_stat_point()
            self.opp_game_sheet.add_stat_point()
        
def main():
    
    man_utd = SoccerGameSheet(Club('Manchester United'))
    
    chelsea = SoccerGameSheet(Club('Chelsea'))
      
    print man_utd
    print chelsea
      
    matchday1 = Match(man_utd, chelsea)
      
    matchday1.goal_home('Wayne Rooney', 15)
    matchday1.goal_home('Memphis Depay', 35)
      
    matchday1.goal_opp('Eden Hazard', 36)
    
    matchday1.halftime()
    
    matchday1.goal_opp('Cesc Fabregas', 57)
      
    matchday1.goal_home('Juan Mata', 75)
    matchday1.goal_home('Ander Herrera', 83)
    matchday1.goal_home('Wayne Rooney', 90)
      
    matchday1.final_score()
    
    print
    print man_utd
    print chelsea
    

if __name__ == '__main__':
    main()