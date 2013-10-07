from numpy import *
from matplotlib.pyplot import *




class Burndown_chart:
	def __init__(self, name, start_day, end_day, initial_number_of_story_points):
		self.name = name;
		self.start_day = start_day;
		self.end_day = end_day;
		self.initial_number_of_story_points = initial_number_of_story_points;
		self.time_axis = linspace(start_day, end_day, (end_day-start_day))
		self.calculate_linear_burn_down();
		self.number_of_story_points_burned = 0;
		self.chart_y = [initial_number_of_story_points]
		self.chart_time_axis= [start_day] 
		
		
	def calculate_linear_burn_down(self):
		self.linear_burn_down_y = linspace(self.initial_number_of_story_points, 0, (self.end_day- self.start_day))
	
	def plot_linear_burn_down(self):
		plot(self.time_axis,self.linear_burn_down_y)
		title("Burndown chart for %s"%self.name)
		xlabel("Days")
		ylabel("Storypoints")
		legend(['Linear burn down'])
		show()
	def burn_story_points(self, number_burned_since_last_update, day):
		self.number_of_story_points_burned += number_burned_since_last_update;
		self.update_chart(day)
	def update_chart(self,day):
		start = len(self.chart_y)
		for i in range(start, day):
			self.chart_y.append(self.chart_y[start-1])
			self.chart_time_axis.append(i)
		self.chart_y.append(self.initial_number_of_story_points-self.number_of_story_points_burned);
		self.chart_time_axis.append(day)
	def plot_chart(self):		
		plot(self.time_axis,self.linear_burn_down_y)
		hold('on')
		plot(self.chart_time_axis, self.chart_y)
		title("Burndown chart for %s"%self.name)
		xlabel("Days")
		ylabel("Storypoints")
		legend(['Linear burn down', "Real burn down"])
		show()
		
		


chart = Burndown_chart(name="Mathilde",start_day=1,end_day=7,initial_number_of_story_points=26)
chart.burn_story_points(4, 3)
chart.burn_story_points(10, 5)
chart.burn_story_points(-3, 6)


chart.plot_chart()
