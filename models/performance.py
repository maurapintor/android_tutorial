from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve, auc, confusion_matrix, f1_score, precision_score
import numpy as np


def plot_roc(y_true, scores, title="Roc"):
    fpr, tpr, th = roc_curve(y_true, scores)
    roc_auc = auc(fpr, tpr)

    plt.plot(fpr, tpr, color="darkorange", lw=2, label=f"AUC = {roc_auc:0.2f}")
    plt.axvline(fpr[np.argmin(np.abs(th))], color="k", linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()
    plt.clf()


def get_metrics(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    print("-" * 30)
    print(f"F1 Score: {f1_score(y_true, y_pred):.4f}")
    print(f"Precision: {precision_score(y_true, y_pred):.4f}")
    print(f"TPR: {tp / (tp + fn):.4f}")
    print(f"FPR: {fp / (fp + tn):.4f}")
    print("-" * 30)
