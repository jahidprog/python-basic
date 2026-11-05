# Machine Learning (ML)

This folder is organized by the kind of feedback a model learns from. The three categories below are useful starting points for deciding where a topic or algorithm belongs.

## Folder guide

| Folder | What the learner receives | Typical goal |
|---|---|---|
| [`Supervised/`](Supervised/) | Examples containing inputs and known target answers (labels) | Predict a target for new inputs |
| [`Unsupervised/`](Unsupervised/) | Inputs without target answers | Find structure, groups, or compact representations in the data |
| [`Reinforcement/`](Reinforcement/) | Feedback from actions taken in an environment, often as rewards | Learn actions that improve long-term outcomes |

## Supervised learning

In supervised learning, a training dataset contains pairs `(X, y)`: `X` is one or more input features, and `y` is the answer the model should learn to predict. During training, the model produces predictions, compares them with the known answers using a loss function, and adjusts its parameters to reduce that loss. The goal is to generalize: perform well on examples that were not used for training.

Two common supervised problem types are:

- **Regression:** the target is a numeric quantity, such as a house price or temperature. Linear regression is a regression method.
- **Classification:** the target is a class or category, such as whether an email is spam or which object appears in an image.

Evaluation should use data kept separate from training. Regression is often assessed with measures of prediction error; classification is often assessed by counting correct and incorrect class predictions and considering precision, recall, or related measures. The right measure depends on the task and the cost of different mistakes.

The existing [`Supervised/LinearRegression/linear_regression_fundamentals.md`](Supervised/LinearRegression/linear_regression_fundamentals.md) note covers a supervised regression method, its prediction equation, squared-error cost, and a worked example.

## Unsupervised learning

Unsupervised learning starts with `X` but has no supplied target `y` for each example. The method looks for patterns or structure using the inputs themselves. Since there are no known answers to compare predictions against, judging results often requires domain knowledge, visual inspection, or task-specific measures.

Common goals include:

- **Clustering:** group examples that are similar under a chosen representation or distance measure.
- **Dimensionality reduction:** describe data with fewer values while retaining useful structure.
- **Anomaly detection:** identify examples that differ substantially from the usual patterns.

Clusters are not automatically meaningful real-world categories; interpretation depends on the data, features, and chosen method. This folder is ready for notes on these topics.

## Reinforcement learning

In reinforcement learning, an **agent** interacts with an **environment**. At each step, the agent observes a state, chooses an action, and receives a reward and a new observation or state. The agent learns a **policy**: a rule for choosing actions. It aims to maximize cumulative reward over time, so an action may be valuable because of rewards it makes possible later.

This differs from ordinary supervised learning because the agent is not simply given the correct action for every situation. It must learn from the consequences of its actions. A key challenge is balancing **exploration** (trying actions to learn what happens) with **exploitation** (using actions already believed to work well).

Reinforcement learning is used when decisions affect what happens next, such as control, sequential planning, or game-playing tasks. A reward is only a proxy for the desired outcome, so it needs to be designed carefully. This folder is ready for future notes.

## How to place a topic

Ask what feedback is available while learning:

1. Are input examples paired with known answers? Put the topic under **Supervised**.
2. Are there inputs but no target answers, and the aim is to discover structure? Put it under **Unsupervised**.
3. Does a learner choose actions, receive rewards, and affect future states? Put it under **Reinforcement**.

Some projects combine these approaches. Organize a note by the main learning setup it explains, and mention the other setup when that distinction helps.
