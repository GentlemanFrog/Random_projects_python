# libs
library(tidyverse)
library(magrittr)
library(plotly)

df = read_csv("clust_merged.csv", col_select = -1) %>% select(-Label)
features = colnames(df %>% select(-cluster))
names(features) = features

test_results = purrr::imap(features, ~ {
  my_df = df %>% select(cluster, !!.x)
  form = glue::glue("{.x} ~ cluster")
  kruskal.test(as.formula(form), data = my_df) %>% broom::tidy() %>% select(p.value)
})

df %<>% pivot_longer(where(is.numeric))

## Kruskal stats

df %<>% rename(stat = name) %>% mutate(cluster = factor(cluster), stat = factor(stat))

df.res = df %>%
  group_by(cluster, stat) %>%
  summarize(stdev = sd(value),
            median = median(value)) %>%
  ungroup() %>%
  pivot_longer(c(stdev, median))

th = theme(axis.text.x = element_text(angle = 45))


features = unique(df$stat)
plots = purrr::map(features, ~ {
  new_df = df %>%
    filter(stat == .x) %>%
    group_by(cluster, stat) %>%
    summarize(
      median = median(value),
      stdev = sd(value),
      mean = mean(value),
      minimal = min(value),
      maximal = max(value)
    ) %>% ungroup()
  p = ggplot(new_df)
  # aes(x = cluster, y = value, group = cluster)
  new_p = p +
    # geom_violin() +
    geom_boxplot(
      width = 0.1,
      aes(
        x = cluster,
        ymin = minimal,
        ymax = maximal,
        middle = median,
        lower = mean - stdev,
        upper = mean + stdev,
        fill = cluster
      ),
      stat = "identity"
    )
  new_p +
    ggtitle(
      label = glue::glue("Feature: {.x)}"),
      subtitle = paste0(
        "p-value: ",
        scales::label_pvalue(accuracy = 0.0001)(test_results[[.x]]$p.value)
      )
    )
})

plots
