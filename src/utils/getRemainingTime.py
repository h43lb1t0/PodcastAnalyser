
from scipy.stats import linregress

class EssimateRemainingTime:
    """
        calculates, based on the given amount of data,
        how long it will probably take until all episodes have been transcribed
    """

    def __init__(self, processing_times: list, episodes: list) -> None:
        self.processing_times = processing_times
        self.episodes = episodes
        self.estimated_time = 0

    def calculate_estimated_time(self) -> None:
        """
            does the calculation using linear regression
        """
        n = len(self.processing_times)

        # Fit a line to the data using linear regression
        slope, intercept, r_value, p_value, std_err = linregress(range(n), self.processing_times)

        # Calculate the estimated time it will take to process a single element
        estimated_time_per_element = slope + intercept

        # Calculate the number of remaining elements
        num_remaining_elements = len(self.episodes) - n

        # Calculate the total estimated processing time
        self.estimated_time = estimated_time_per_element * num_remaining_elements

    def printTimeEssimation(self) -> None:
        """
            prints the time in the appropriate format
        """
        if self.estimated_time < 60:
            print(f"Esstimated time remaining: {self.estimated_time} sec")
        if self.estimated_time > 60 and self.estimated_time < 3600:
            print(f"Esstimated time remaining: {round(self.estimated_time/60, 2)} min")
        else:
            print(f"Esstimated time remaining: {round((self.estimated_time/60)/60, 2)} h")

    def run(self) -> None:
        """
            stars all needed functions
        """
        self.calculate_estimated_time()
        self.printTimeEssimation()