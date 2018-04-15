import cProfile
import pstats

# Run profiler and save to github.stats
cProfile.run('import github', 'github.stats')
stats = pstats.Stats('github.stats')
# Clean up filenames for the report
stats.strip_dirs()
# Sort the statistics by the cumulative time spent
stats.sort_stats('cumulative')
stats.print_stats()
